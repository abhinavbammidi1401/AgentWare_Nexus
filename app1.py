import streamlit as st
import pandas as pd
from model.warehouse_model import WarehouseModel

st.title("Warehouse Management System")

model = WarehouseModel(5)

# Interface to process orders
st.header("Process Order")
item = st.text_input("Item")
quantity = st.number_input("Quantity", min_value=1, step=1)
if st.button("Process Order"):
    success, message = model.order_processing_agent.process_order(item, quantity)
    if success:
        st.success(f"Order for {quantity} of {item} processed successfully.")
        st.success(message)  # Display transport message
    else:
        st.error(message)
    
    # Ensure inventory status is updated
    model.step()

# Interface to monitor environment
st.header("Monitor Environment")
if st.button("Monitor Environment"):
    message = model.maintenance_agent.monitor_environment()
    st.success(message)  # Display monitoring completion message

# Interface to show inventory status
st.header("Inventory Status")
if st.button("Show Inventory Status"):
    inventory = model.inventory_agent.inventory
    df = pd.DataFrame(list(inventory.items()), columns=["Item", "Quantity"])
    st.dataframe(df)  # Display inventory as a DataFrame
