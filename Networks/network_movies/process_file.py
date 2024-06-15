import sys
import csv
import functions

###########################
## Check input file name ##
###########################

# Check if the user provided a file name as a command-line argument
if len(sys.argv) != 3:
    print("Usage: python create_html.py <input_file_name> <network_file_name>")
    sys.exit(1)
    
input_file_name   = sys.argv[1]
network_file_name = sys.argv[2]

############################
## Process the input file ##
############################

with open(input_file_name, mode = 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    
    building_round_number = 0
    round_events = []
    dict_round_events = {}
    
    for row in reader:
        round_number = row['round_number']
        id_in_group  = row['id_in_group']
        action       = row['action']
        time         = row['time']
        time_ms      = row['time_ms']
        
        if building_round_number != round_number:
            if int(building_round_number) > 0:
                dict_round_events[building_round_number] = round_events
            building_round_number = round_number
            round_events = []
            
        if action != "request":
            if action != "finish":
                round_events.append([id_in_group, action, time, time_ms])
                
    dict_round_events[building_round_number] = round_events

##############################
## Process the network file ##
##############################

with open(network_file_name, mode = 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    
    building_round_number = 0
    round_nodes = []
    dict_round_nodes = {}
    
    for row in reader:
        round_number = row['round']
        node_id      = row['node_id']
        neighbors    = row['neighbors_list']
        position_x   = row['position_x']
        position_y   = row['position_y']
        
        if building_round_number != round_number:
            if int(building_round_number) > 0:
                dict_round_nodes[building_round_number] = round_nodes
            building_round_number = round_number
            round_nodes = []
            
        round_nodes.append([node_id, neighbors, position_x, position_y])
        
    dict_round_nodes[building_round_number] = round_nodes

######################
## Build html files ##
######################

for round_number, round_events in dict_round_events.items():
    output_file_name = "output/ROUND_" + str(round_number) + " " + input_file_name.split(".")[0] + ".html"
    
    round_structure = dict_round_nodes[round_number]
    n_nodes = len(round_structure)
    n_steps = len(round_events)
    
    node_positions_html = functions.plot_node_positions(round_structure)
    node_neighbors_html = functions.plot_node_neighbors(round_structure)
    list_actions_html_1 = functions.plot_list_actions(round_events[  0: 40],   0)
    list_actions_html_2 = functions.plot_list_actions(round_events[ 40: 80],  40)
    list_actions_html_3 = functions.plot_list_actions(round_events[ 80:120],  80)
    list_actions_html_4 = functions.plot_list_actions(round_events[120:160], 120)
    
    #print(list_actions_html)
    #sys.exit(1)

    net_state_html = ""
    net_state = functions.build_net_state(n_nodes)
    net_state_html += functions.plot_net_state(net_state)
    for event in round_events:
        functions.update_net_state(net_state, functions.get_node_label(event[0]), event[1])
        net_state_html += "," + functions.plot_net_state(net_state)
        
    html_file = ( functions.get_html_1() 
                + list_actions_html_1 
                + list_actions_html_2 
                + list_actions_html_3 
                + list_actions_html_4 
                + functions.get_html_2() 
                + node_positions_html 
                + node_neighbors_html 
                + functions.get_html_3(n_steps) 
                + net_state_html 
                + functions.get_html_4()
                )
        
    # Open the specified file in write mode
    with open(output_file_name, "w") as file:
        # Write the HTML content to the file
        file.write(html_file)

    print(f"HTML file '{output_file_name}' has been created.")
    
    
    
    
    
    
    
    
    
    
