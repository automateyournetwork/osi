import wikipedia
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))

# -------------------------
# Template
# -------------------------

wiki_template = env.get_template('wiki.j2')

# -------------------------
# Lists of Wiki Page Titles to Gather blocked by output folder
# -------------------------

generalPages=[
    "List of network protocols (OSI model)",
    "Computer_network",
    "World_Wide_Web",
    "History of the Internet",
    "Encapsulation (networking)",
    "ARPANET",
    "Internet_Engineering_Task_Force",
    "Institute_of_Electrical_and_Electronics_Engineers",
    ]

layerOnePages=[
    "Physical layer",
    "Network_interface_controller",
    "Digital_signal",
    "Transmission_medium",
    "Ethernet_over_twisted_pair",
    "Ethernet_physical_layer",
    "Ethernet",
    "Fast_Ethernet",
    "Gigabit_Ethernet"
    ]

layerTwoPages=[
    "Data_link_layer",
    "Frame_(networking)",
    "Network_switch",
    "Network_address",
    "Local_area_network",
    "Virtual_LAN",
    "Medium_access_control",
    "Logical_link_control",
    "Multiplexing",
    "Broadcast_domain",
    "Frame_check_sequence",
    "Collision_domain",
    "Address_Resolution_Protocol",
    "Duplex_(telecommunications)",
    "Carrier-sense_multiple_access_with_collision_detection",
    "Carrier-sense_multiple_access_with_collision_avoidance",
    ]

layerThreePages=[
    "Network_layer",
    "Network_packet",
    "Subnetwork",
    "Mask_(computing)",
    "Dot-decimal_notation",
    "Bit_numbering",
    "Internet_Protocol_version_4",
    "Internet_Protocol_version_6",
    "Classless_Inter-Domain_Routing",
    "Classful_network",
    "Packet_forwarding",
    "Routing",
    "Router_(computing)",
    "IP_routing",
    "Internet_Protocol",
    "Static_Routing",
    "Dynamic_routing",
    "Routing_protocol",
    "Routing_table",
    "Open Shortest Path First",
    "Routing_Information_Protocol",
    "Border_Gateway_Protocol",
    "Enhanced_Interior_Gateway_Routing_Protocol",
    "Intermediate_system_to_intermediate_system",
    "Interior_gateway_protocol",
    "Interior_Gateway_Routing_Protocol",
    "Exterior_gateway_protocol",
    "Link_state_routing_protocol",
    "Distance-vector_routing_protocol",
    "Path-vector_routing_protocol",
    "Unicast",
    "Broadcasting_(networking)",
    "Multicast",
    "Anycast_(networking)",
    "Metrics_(networking)",
    "Multipath_routing",
    "Equal-cost_multi-path_routing",
    "Autonomous_system_(Internet)",
    "ip address",
    ]

layerFourPages=[
    "Transport_layer",
    "Firewall (computing)",
    "User Datagram Protocol",
    "Transmission Control Protocol",
    "Flow_control_(data)",
    "Reliability_(computer_networking)",
    "State_(computer_science)",
    ]

layerFivePages=[
    "Session_layer",
    "Remote_procedure_call",
    "Authentication",
    "Authorization",
    "NetBIOS",
    "Point-to-Point_Tunneling_Protocol"
    ]

layerSixPages=[
    "Presentation_layer",
    "Character_encoding",
    "Data_conversion",
    "EBCDIC"
    ]

layerSevenPages=[
    "Application_layer",
    "Domain_Name_System",
    "Domain_name",
    "File_Transfer_Protocol",
    "Hypertext_Transfer_Protocol",
    "HTTPS",
    "Lightweight_Directory_Access_Protocol",
    "Network_News_Transfer_Protocol",
    "Network_Time_Protocol",
    "Post_Office_Protocol",
    "Simple_Mail_Transfer_Protocol",
    "Simple_Network_Management_Protocol",
    "Secure_Shell",
    "Telnet",
    "Transport_Layer_Security",
    "Gopher_(protocol)",
    "Internet_Relay_Chat",
    "Dynamic_Host_Configuration_Protocol",
    ]                

for page in generalPages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------

    with open(f"OSI/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()

for page in layerOnePages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------

    with open(f"OSI/01 Physical/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()

for page in layerTwoPages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------

    with open(f"OSI/02 Data/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close() 

for page in layerThreePages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------    

    with open(f"OSI/03 Network/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()

for page in layerFourPages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------    

    with open(f"OSI/04 Transport/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()

for page in layerFivePages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------    

    with open(f"OSI/05 Session/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()

for page in layerSixPages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------    

    with open(f"OSI/06 Presentation/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()

for page in layerSevenPages:
    rawPage = wikipedia.page(f"{ page }")
    wikiTitle = rawPage.title
    wikiURL = rawPage.url
    wikiContent = json.dumps(rawPage.content)
    wikiLinks = rawPage.links
    wikiSummary = rawPage.summary
    wikiCategory = rawPage.categories
    wikiReferences = rawPage.references
    wikiImages = rawPage.images
    print(page)

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

    parsed_output = wiki_template.render(
        title = wikiTitle,
        summary = wikiSummary,
        category = wikiCategory,
        refs = wikiReferences,
        URL = wikiURL,
        content = wikiContent,
        links = wikiLinks,
        images = wikiImages
    )

# -------------------------
# Save the markdown file
# -------------------------    

    with open(f"OSI/07 Application/{ page }.md".replace('_',' '), "w", errors='ignore') as fh:
        fh.write(parsed_output)               
        fh.close()