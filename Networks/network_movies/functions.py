########################
## Auxiliar functions ##
########################

def get_node_label(node_id):
    if int(node_id) < 10:
        return "P0" + str(node_id)
    else:
        return "P" + str(node_id)
        
def build_net_state(nodes):
    net_state = {}
    for node_id in list(range(1,nodes+1)):
        net_state[get_node_label(node_id)] = 0
    return net_state
    
def update_net_state(net_state, node, action):
    if action == "white":
        net_state[node] = 0
    if action == "blue":
        net_state[node] = 1
    if action == "red":
        net_state[node] = 2
    if action == "brown":
        net_state[node] = 3
    if action == "indigo":
        net_state[node] = 4
    if action == "orange":
        net_state[node] = 5
    if action == "green":
        net_state[node] = 6
    if action == "cyan":
        net_state[node] = 7
    if action == "pink":
        net_state[node] = 8
    if action == "purple":
        net_state[node] = 9
    if action == "yellow":
        net_state[node] = 10
    if action == "silver":
        net_state[node] = 11
    if action == "teal":
        net_state[node] = 12
    if action == "black":
        net_state[node] = 13
    if action == "magenta":
        net_state[node] = 14
    if action == "olive":
        net_state[node] = 15
    if action == "beige":
        net_state[node] = 16
    
def plot_net_state(net_state):
    output = "["
    for node_id, action in net_state.items():
        output += "{ id: '" + node_id + "', type: " + str(action) + " },"
    output = output[:-1]
    output += "]"
    return output
    
def plot_node_positions(net_structure):
    output = "nodes: ["
    for node_id, neighbors, position_x, position_y in net_structure:
        output += "{ id: '" + get_node_label(node_id) + "', type: 0, x: " + position_x + ", y: " + position_y + " },"
    output += "],"
    return output
    
def plot_node_neighbors(net_structure):
    output = "links: ["
    for node_id, neighbors, position_x, position_y in net_structure:
        for neighbor in neighbors.split(","):
            output += "{ source: '" + get_node_label(node_id) + "', target: '" + get_node_label(neighbor) + "' },"
    output += "]"
    return output
    
def plot_list_actions(round_events, n):
    output = "<ul>"
    count = n
    for node_id, action, time, time_ms in round_events:
        count = count + 1
        output += '<li id="li' + str(count) + '">' + get_node_label(node_id) + ' : ' + action + ' : ' + time + ' : ' + time_ms + '</li>'
    output += "</ul>"
    return output

def get_html_1():
    return """
<!DOCTYPE html>
<html>
	<head>
		<title>History Network</title>
		<style>
			.node {
				stroke: #999;
				stroke-width: 2px;
			}
			.type-0 {
				fill: #ffffff;
			}
			.type-1 {
				fill: #3377ff;
			}
			.type-2 {
				fill: #ff002b;
			}
			.type-3 {
				fill: #a52a2a;
			}
			.type-4 {
				fill: #4b0082;
			}
			.type-5 {
				fill: #ff8c00;
			}
			.type-6 {
				fill: #008000;
			}
			.type-7 {
				fill: #00ffff;
			}
			.type-8 {
				fill: #ffc0cb;
			}
			.type-9 {
				fill: #800080;
			}
			.type-10 {
				fill: #ffff00;
			}
			.type-11 {
				fill: #c0c0c0;
			}
			.type-12 {
				fill: #008080;
			}
			.type-13 {
				fill: #000000;
			}
			.type-14 {
				fill: #ff00ff;
			}
			.type-15 {
				fill: #808000;
			}
			.type-16 {
				fill: #c8c8a2;
			}
			
			.label {
				font-family: Arial, sans-serif;
				font-size: 12px;
				text-anchor: middle;
				dominant-baseline: central;
			}
			.link {
				fill: none;
				stroke: #999;
				stroke-width: 2px;
			}
			.node-border {
				fill: none;
				stroke: #999;
				stroke-width: 2px;
			}
			svg {
				border: solid 2px black;
			}
			ul {
				position: fixed;
				top: 0px;
				left: 820px;
				z-index: 1;
			}
			ul + ul {
				position: fixed;
				top: 0px;
				left: 1040px;
				z-index: 1;
			}
			ul + ul + ul {
				position: fixed;
				top: 0px;
				left: 1280px;
				z-index: 1;
			}
			ul + ul + ul + ul {
				position: fixed;
				top: 0px;
				left: 1520px;
				z-index: 1;
			}
            .active {
                background-color: yellow;
            }
		</style>
		<script src="https://d3js.org/d3.v7.min.js"></script>
		<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
	</head>
	<body>
"""

def get_html_2():
    return """
		<script>
			const graphData = {
"""

def get_html_3(n_steps):
    return """
			};

			const width =  800;
			const height = 800;

			// Set up the SVG container
			const svg = d3.select("body").append("svg")
				.attr("width", width)
				.attr("height", height);

			// Create the network graph
			const link = svg.selectAll(".link")
				.data(graphData.links)
				.enter().append("line")
				.attr("class", "link")
				.style("stroke", "#999")
				.style("stroke-width", 2)
				.attr("x1", d => graphData.nodes.find(node => node.id === d.source).x)
				.attr("y1", d => graphData.nodes.find(node => node.id === d.source).y)
				.attr("x2", d => graphData.nodes.find(node => node.id === d.target).x)
				.attr("y2", d => graphData.nodes.find(node => node.id === d.target).y);


			const nodeBorder = svg.selectAll(".node-border")
				.data(graphData.nodes)
				.enter().append("circle")
				.attr('class', 'node-border')
				.attr("r", 32)
				.attr("cx", d => d.x)
				.attr("cy", d => d.y);
				

			const node = svg.selectAll(".node")
				.data(graphData.nodes)
				.enter().append("circle")
				.attr('class', d => `node type-${d.type}`)
				.attr('id', d => `${d.id}`)
				.attr("r", 30)
				.attr("cx", d => d.x)
				.attr("cy", d => d.y);
				

			const label = svg.selectAll(".label")
				.data(graphData.nodes)
				.enter().append("text")
				.attr("class", "label")
				.attr("dy", ".1em")
				.text(d => d.id)
				.attr("x", d => d.x)
				.attr("y", d => d.y);

		</script>
        <br><br>
		<div>Current: <span id="Current">0</span>/<span>""" + str(n_steps) + """</total></div>
        <br>
        <button id="Start">Start</button>
        <button id="Prev">Prev</button>
		<button id="Next">Next</button>
        <b>|</b>
        <button id="Auto05">Auto05</button>
        <button id="Auto1">Auto1</button>
        <button id="Auto2">Auto2</button>
        <button id="Stop">Stop</button>
		
		<script>
			const historyData = [
"""

def get_html_4():
    return """
			]
		</script>
		<script>
			var current = 0;
            var interval;
			$( "#Start" ).on( "click", function() {
				current = 0;
				$('#Current').text(current);
				load_history(current);
			});
			$( "#Prev" ).on( "click", function() {
				current = current - 1;
				if (current < 0) { current = 0; }
				$('#Current').text(current);
				load_history(current);
			});
			$( "#Next" ).on( "click", function() {
				current = current + 1;
				if (current > historyData.length - 1) { current = historyData.length - 1; }
				$('#Current').text(current);
				load_history(current);
			});
			$( "#Auto05" ).on( "click", function() {
                clearInterval(interval);
                interval = setInterval(function(){
                    current = current + 1;
                    if (current > historyData.length - 1) { current = historyData.length - 1; }
                    $('#Current').text(current);
                    load_history(current);
                }, 500);
			});
			$( "#Auto1" ).on( "click", function() {
                clearInterval(interval);
                interval = setInterval(function(){
                    current = current + 1;
                    if (current > historyData.length - 1) { current = historyData.length - 1; }
                    $('#Current').text(current);
                    load_history(current);
                }, 1000);
			});
			$( "#Auto2" ).on( "click", function() {
                clearInterval(interval);
                interval = setInterval(function(){
                    current = current + 1;
                    if (current > historyData.length - 1) { current = historyData.length - 1; }
                    $('#Current').text(current);
                    load_history(current);
                }, 2000);
			});
			$( "#Stop" ).on( "click", function() {
                clearInterval(interval);
			});
			
			function load_history(target) {
				state = historyData[target];
				for (const [key, value] of Object.entries(state)) {
					$('#' + value.id).removeClass('type-0');
					$('#' + value.id).removeClass('type-1');
					$('#' + value.id).removeClass('type-2');
					$('#' + value.id).removeClass('type-3');
					$('#' + value.id).removeClass('type-4');
					$('#' + value.id).removeClass('type-5');
					$('#' + value.id).removeClass('type-6');
					$('#' + value.id).removeClass('type-7');
					$('#' + value.id).removeClass('type-8');
					$('#' + value.id).removeClass('type-9');
					$('#' + value.id).removeClass('type-10');
					$('#' + value.id).removeClass('type-11');
					$('#' + value.id).removeClass('type-12');
					$('#' + value.id).removeClass('type-13');
					$('#' + value.id).removeClass('type-14');
					$('#' + value.id).removeClass('type-15');
					$('#' + value.id).removeClass('type-16');
					$('#' + value.id).addClass('type-' + value.type);
				}
                $('li').removeClass('active');
                $('#li' + target).addClass('active');
			}
		</script>
	</body>
</html>
"""