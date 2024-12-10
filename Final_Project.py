import streamlit as st

# Page title
st.set_page_config(page_title="ML Model Generator", layout="wide")
st.title("ML Model Generator")
st.info("Please generate data using the sidebar button to view visualizations and results.")

# Sidebar
with st.sidebar:
    st.header("Data Source")
    data_source = st.radio(
        "Choose data source:",
        options=["Generate Synthetic Data", "Upload Dataset"],
        index=0
    )

    if data_source == "Generate Synthetic Data":
        st.subheader("Synthetic Data Generation")
        st.text("Set parameters for synthetic data generation.")
        
        st.subheader("Data Generation Parameters")
        feature_names = st.text_input(
            "Enter feature names (comma-separated)",
            placeholder="e.g., length (mm), width (mm), density (g/cm³)"
        )
        class_names = st.text_input(
            "Enter class names (comma-separated)",
            placeholder="e.g., Ampalaya, Banana, Cabbage"
        )

        # Class-specific settings
        st.subheader("Class-Specific Settings")
        classes = class_names.split(", ")
        for cls in classes:
            if cls:
                with st.expander(f"{cls} Settings"):
                    st.slider(f"{cls} sample size", min_value=10, max_value=1000, value=100)
                    st.slider(f"{cls} feature range", min_value=0.0, max_value=10.0, value=(1.0, 5.0))

    # Train/Test Split Configuration
    st.subheader("Sample Size & Train/Test Split Configuration")
    total_samples = st.slider("Number of samples", 100, 10000, 1000, step=100)
    test_size_percentage = st.slider("Test Size (%)", 10, 90, 30)
    train_size_percentage = 100 - test_size_percentage

    st.write(f"Train: {train_size_percentage}% / Test: {test_size_percentage}%")

    # Button to generate data
    if st.button("Generate Data and Train Models"):
        st.success("Data generated and models trained successfully!")

# Main panel placeholder (for charts, tables, etc.)
st.write("Visualization and results will appear here after data generation.")
