# AgentWare Nexus - Warehouse Management Multiagent System

This project implements a warehouse management system using a multiagent approach with the Mesa framework. The system simulates the interactions between different agents responsible for inventory management, order processing, and maintenance.

## Project Structure

warehouse_management/
│
├── agents/
│   ├── __init__.py
│   ├── inventory_agent.py
│   ├── order_processing_agent.py
│   └── transport_agent.py
│   └── maintenance_agent.py
│
├── model/
│   ├── __init__.py
│   └── warehouse_model.py
│
├── app.py
├── requirements.txt
└── README.md

### **'agents\'**: This directory contains the agent classes responsible for different tasks within the warehouse:
- 'InventoryAgent': Manages inventory levels and updates.
- 'OrderProcessingAgent': Processes customer orders by checking inventory and coordinating with the transport agent.
- 'TransportAgent': Simulates the transportation of items to the dispatch area.
- 'MaintenanceAgent': Monitors the warehouse environment and ensures operational stability.

2. **'model\'**: Contains the model class that orchestrates the interactions between agents:
- 'WarehouseModel': A Mesa model that instances of all agents and manages the overall simulation.

3. **'app.py'**: The Streamlit interface to interact with the multiagent system. This file allows users to process orders, monitor the environment, and check inventory status.

4. **'requirements.txt'**: Lists all the Python dependencies required to run the project.