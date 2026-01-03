import streamlit as st

st.title("📤 Upload Pump Information")

st.markdown("---")

# File Upload Section
st.subheader("📁 Upload Files")
st.markdown("Upload pump documentation, specifications, or data files.")

uploaded_files = st.file_uploader(
    "Choose files to upload",
    type=["pdf", "docx", "xlsx", "csv", "txt", "jpg", "png"],
    accept_multiple_files=True,
    help="Supported formats: PDF, Word, Excel, CSV, Text, Images"
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} file(s) selected")
    
    # Display uploaded files
    with st.expander("View Uploaded Files"):
        for idx, file in enumerate(uploaded_files, 1):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{idx}. {file.name}**")
            with col2:
                st.write(f"Size: {file.size / 1024:.2f} KB")
            with col3:
                st.download_button(
                    label="Download",
                    data=file.getvalue(),
                    file_name=file.name,
                    key=f"download_{idx}",
                    mime=file.type
                )

st.markdown("---")

# Pump Information Form
st.subheader("📝 Pump Information")

with st.form("pump_information_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        pump_name = st.text_input(
            "Pump Name/Model",
            placeholder="e.g., Model XYZ-123",
            help="Enter the pump model or name"
        )
        
        brand = st.text_input(
            "Brand",
            placeholder="e.g., Brand Name",
            help="Enter the manufacturer brand"
        )
        
        application_area = st.selectbox(
            "Application Area",
            options=["Select application area...", "Residential", "Commercial", "Industrial", "Agricultural", "Other"],
            help="Select the primary application area"
        )
    
    with col2:
        serial_number = st.text_input(
            "Serial Number",
            placeholder="e.g., SN-123456",
            help="Enter the pump serial number"
        )
        
        manufacturer = st.text_input(
            "Manufacturer",
            placeholder="e.g., Manufacturer Name",
            help="Enter the manufacturer name"
        )
        
        pump_type = st.selectbox(
            "Pump Type",
            options=["Select pump type...", "Centrifugal", "Submersible", "Jet", "Diaphragm", "Other"],
            help="Select the type of pump"
        )
    
    st.markdown("---")
    
    # Physical Dimensions
    st.markdown("### Physical Dimensions")
    dim_col1, dim_col2, dim_col3 = st.columns(3)
    
    with dim_col1:
        length_col1, length_col2 = st.columns([3, 1])
        with length_col1:
            length = st.number_input("Length", min_value=0.0, value=0.0, step=0.1, key="length")
        with length_col2:
            length_unit = st.selectbox("", options=["mm", "cm", "m"], key="length_unit", label_visibility="collapsed")
        st.caption("(l)")
    
    with dim_col2:
        width_col1, width_col2 = st.columns([3, 1])
        with width_col1:
            width = st.number_input("Width", min_value=0.0, value=0.0, step=0.1, key="width")
        with width_col2:
            width_unit = st.selectbox("", options=["mm", "cm", "m"], key="width_unit", label_visibility="collapsed")
        st.caption("(w)")
    
    with dim_col3:
        height_col1, height_col2 = st.columns([3, 1])
        with height_col1:
            height = st.number_input("Height", min_value=0.0, value=0.0, step=0.1, key="height")
        with height_col2:
            height_unit = st.selectbox("", options=["mm", "cm", "m"], key="height_unit", label_visibility="collapsed")
        st.caption("(h)")
    
    st.markdown("---")
    
    # Performance Specifications
    st.markdown("### Performance Specifications")
    perf_col1, perf_col2 = st.columns(2)
    
    with perf_col1:
        flow_col1, flow_col2 = st.columns([3, 1])
        with flow_col1:
            flow_rate = st.number_input("Flow Rate", min_value=0.0, value=0.0, step=0.1, key="flow_rate")
        with flow_col2:
            flow_unit = st.selectbox("", options=["l/s", "l/min", "m³/h", "gpm"], key="flow_unit", label_visibility="collapsed")
        st.caption("Flow rate")
    
    with perf_col2:
        head_col1, head_col2 = st.columns([3, 1])
        with head_col1:
            head = st.number_input("Head", min_value=0.0, value=0.0, step=0.1, key="head")
        with head_col2:
            head_unit = st.selectbox("", options=["m", "ft"], key="head_unit", label_visibility="collapsed")
        st.caption("Head")
    
    st.markdown("---")
    
    # Additional Information
    st.markdown("### Additional Information")
    additional_notes = st.text_area(
        "Notes/Comments",
        placeholder="Enter any additional information, specifications, or notes about the pump...",
        height=100,
        help="Add any additional details or comments"
    )
    
    st.markdown("---")
    
    # Submit Button
    submitted = st.form_submit_button("💾 Submit Information", use_container_width=True)
    
    if submitted:
        # Validation
        if not pump_name:
            st.error("⚠️ Please enter a pump name/model")
        elif application_area == "Select application area...":
            st.error("⚠️ Please select an application area")
        elif pump_type == "Select pump type...":
            st.error("⚠️ Please select a pump type")
        else:
            # Store data in session state
            pump_data = {
                "pump_name": pump_name,
                "brand": brand,
                "serial_number": serial_number,
                "manufacturer": manufacturer,
                "application_area": application_area,
                "pump_type": pump_type,
                "dimensions": {
                    "length": length,
                    "length_unit": length_unit,
                    "width": width,
                    "width_unit": width_unit,
                    "height": height,
                    "height_unit": height_unit
                },
                "performance": {
                    "flow_rate": flow_rate,
                    "flow_unit": flow_unit,
                    "head": head,
                    "head_unit": head_unit
                },
                "notes": additional_notes,
                "files": [f.name for f in uploaded_files] if uploaded_files else []
            }
            
            # Initialize session state if needed
            if "uploaded_pumps" not in st.session_state:
                st.session_state.uploaded_pumps = []
            
            st.session_state.uploaded_pumps.append(pump_data)
            
            st.success("✅ Pump information submitted successfully!")
            st.balloons()
            
            # Display summary
            with st.expander("📋 View Submitted Information"):
                st.json(pump_data)

