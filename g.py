import streamlit as st
from PIL import Image

# Set the page title
st.title("Test Scenario Description Tool")

# Case 1: Text box for optional context
context = st.text_area("Optional Context", placeholder="Enter any additional context here...")

# Case 2: Multi-image uploader for screenshots (required)
uploaded_files = st.file_uploader("Upload screenshots (required)", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

# Case 3: Button to describe testing instructions
if st.button("Describe Testing Instructions"):
    if len(uploaded_files) == 0:
        st.error("Please upload at least one screenshot to proceed.")
    else:
        st.success("Test instructions are generated based on the inputs.")
        
        # Display the context if provided
        if context:
            st.write(f"**Context provided:** {context}")
        
        # Process uploaded images
        st.write("**Uploaded screenshots:**")
        for uploaded_file in uploaded_files:
            # Open the image using PIL
            image = Image.open(uploaded_file)
            
            
            # Display the image
            st.image(image, caption=f"Uploaded image: {uploaded_file.name}", use_column_width=True)
            
            # Extract basic information from the image
            width, height = image.size
            file_info = f"Image: {uploaded_file.name}, Dimensions: {width}x{height}px, Size: {uploaded_file.size / 1024:.2f} KB"
            st.write(file_info)
        
        # Example: Generate test scenario based on the context and uploaded images
        st.write("### Generated Test Scenario:")
        scenario_text = """
        1. Navigate to the application and log in if necessary.
        2. Open the screen where the screenshot was taken.
        3. Verify that the UI appears as shown in the uploaded screenshot(s).
        4. Check that all buttons, text, and layout elements are correctly displayed as per the image dimensions.
        5. If the optional context is provided, follow any additional instructions given:
        """

        # Append context to the test scenario if available
        if context:
            scenario_text += f"\n\n**Context Provided:** {context}\n"

        # Append information about each image to the test scenario
        for uploaded_file in uploaded_files:
            scenario_text += f"\n- Verify visual correctness for the screenshot `{uploaded_file.name}`."

        st.write(scenario_text)
