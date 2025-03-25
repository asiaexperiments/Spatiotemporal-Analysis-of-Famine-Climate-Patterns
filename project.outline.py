from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Spatiotemporal Data Pipeline')

# Nodes
dot.node('A', '1. Data Collection\n(Dryad, FAO, ReliefWeb)')
dot.node('B', '2. Cleaning & Integration\n(Merge by location/time)')
dot.node('C', '3. Feature Engineering\n(Create climate & famine indicators)')
dot.node('D', '4. Spatiotemporal Analysis\n(GIS, clustering, trend analysis)')
dot.node('E', '5. Visualization\n(Maps, heatmaps, timelines)')
dot.node('F', '6. (Optional) Prediction\n(Risk zones, early warnings)')

# Edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F', style='dashed')  # Optional step

# Save and render
dot.render('spatiotemporal_pipeline', format='png', cleanup=True)
dot.view()
