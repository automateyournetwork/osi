import wikipedia
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))

# -------------------------
# Templates
# -------------------------

protocolList_template = env.get_template('Protocol_List.j2')
layer_template = env.get_template('Layer.j2')

protocolList = wikipedia.page("List of network protocols (OSI model)")
wikiTitle = protocolList.title
wikiURL = protocolList.url
wikiContent = json.dumps(protocolList.content)
wikiLinks = protocolList.links
wikiSummary = protocolList.summary
wikiCategory = protocolList.categories
wikiReferences = protocolList.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = protocolList_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/OSI Protocol List.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()


layerOne = wikipedia.page("Physical layer")
wikiTitle = layerOne.title
wikiURL = layerOne.url
wikiContent = json.dumps(layerOne.content)
wikiLinks = layerOne.links
wikiSummary = json.dumps(layerOne.summary)
wikiCategory = layerOne.categories
wikiReferences = layerOne.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 01.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerTwo = wikipedia.page("Data_link_layer")
wikiTitle = layerTwo.title
wikiURL = layerTwo.url
wikiContent = json.dumps(layerTwo.content)
wikiLinks = layerTwo.links
wikiSummary = json.dumps(layerTwo.summary)
wikiCategory = layerTwo.categories
wikiReferences = layerTwo.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 02.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerThree = wikipedia.page("Network_layer")
wikiTitle = layerThree.title
wikiURL = layerThree.url
wikiContent = json.dumps(layerThree.content)
wikiLinks = layerThree.links
wikiSummary = json.dumps(layerThree.summary)
wikiCategory = layerThree.categories
wikiReferences = layerThree.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 03.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerFour = wikipedia.page("Transport_layer")
wikiTitle = layerFour.title
wikiURL = layerFour.url
wikiContent = json.dumps(layerFour.content)
wikiLinks = layerFour.links
wikiSummary = json.dumps(layerFour.summary)
wikiCategory = layerFour.categories
wikiReferences = layerFour.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 04.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerFive = wikipedia.page("Session_layer")
wikiTitle = layerFive.title
wikiURL = layerFive.url
wikiContent = json.dumps(layerFive.content)
wikiLinks = layerFive.links
wikiSummary = json.dumps(layerFive.summary)
wikiCategory = layerFive.categories
wikiReferences = layerFive.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 05.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerFive = wikipedia.page("Session_layer")
wikiTitle = layerFive.title
wikiURL = layerFive.url
wikiContent = json.dumps(layerFive.content)
wikiLinks = layerFive.links
wikiSummary = json.dumps(layerFive.summary)
wikiCategory = layerFive.categories
wikiReferences = layerFive.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 05.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerSix = wikipedia.page("Presentation_layer")
wikiTitle = layerSix.title
wikiURL = layerSix.url
wikiContent = json.dumps(layerSix.content)
wikiLinks = layerSix.links
wikiSummary = json.dumps(layerSix.summary)
wikiCategory = layerSix.categories
wikiReferences = layerSix.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 06.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

layerSeven = wikipedia.page("Application_layer")
wikiTitle = layerSeven.title
wikiURL = layerSeven.url
wikiContent = json.dumps(layerSeven.content)
wikiLinks = layerSeven.links
wikiSummary = json.dumps(layerSeven.summary)
wikiCategory = layerSeven.categories
wikiReferences = layerSeven.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("OSI/Layer 07.md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

ospf = wikipedia.page("Open Shortest Path First")
wikiTitle = ospf.title
wikiURL = ospf.url
wikiContent = json.dumps(ospf.content)
wikiLinks = ospf.links
wikiSummary = json.dumps(ospf.summary)
wikiCategory = ospf.categories
wikiReferences = ospf.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("Routing Protocols/Open Shortest Path First (OSPF).md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

rip = wikipedia.page("Routing_Information_Protocol")
wikiTitle = rip.title
wikiURL = rip.url
wikiContent = json.dumps(rip.content)
wikiLinks = rip.links
wikiSummary = json.dumps(rip.summary)
wikiCategory = rip.categories
wikiReferences = rip.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("Routing Protocols/Routing Information Protocol (RIP).md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

bgp = wikipedia.page("Border_Gateway_Protocol")
wikiTitle = bgp.title
wikiURL = bgp.url
wikiContent = json.dumps(bgp.content)
wikiLinks = bgp.links
wikiSummary = json.dumps(bgp.summary)
wikiCategory = bgp.categories
wikiReferences = bgp.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("Routing Protocols/Border Gateway Protocol (BGP).md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

eigrp = wikipedia.page("Enhanced_Interior_Gateway_Routing_Protocol")
wikiTitle = eigrp.title
wikiURL = eigrp.url
wikiContent = json.dumps(eigrp.content)
wikiLinks = eigrp.links
wikiSummary = json.dumps(eigrp.summary)
wikiCategory = eigrp.categories
wikiReferences = eigrp.references

# -------------------------
# Pass to Jinja2 Template 
# -------------------------

parsed_output = layer_template.render(
    title = wikiTitle,
    summary = wikiSummary,
    category = wikiCategory,
    refs = wikiReferences,
    URL = wikiURL,
    content = wikiContent,
    links = wikiLinks
)

# -------------------------
# Save the markdown file
# -------------------------

with open("Routing Protocols/Enhanced Interior Gateway Routing Protocol (EIGRP).md", "w") as fh:
    fh.write(parsed_output)               
    fh.close()

#print(wikipedia.search("RIP"))