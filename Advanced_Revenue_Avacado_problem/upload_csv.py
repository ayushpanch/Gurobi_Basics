import streamlit as st
import pandas as pd
import base64

def calculate_sum(row):
    return row['A'] + row['B'] + row['C'] + row['D']

def main():
    st.title("CSV Sum Calculator")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file)

        # Add a new column for the sum
        df['Result'] = df.apply(calculate_sum, axis=1)

        # Display the original and modified data
        st.write("Original Data:")
        st.write(df.drop(columns=['Result'], errors='ignore'))  # Display without the Result column

        st.write("Data with Sum (Result) Column:")
        st.write(df)

        # Compile button to download the modified CSV file
        if st.button("Compile"):
            # Create a link for downloading the modified CSV
            csv_data = df.to_csv(index=False).encode()
            b64 = base64.b64encode(csv_data).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="compiled_data.csv">Download Compiled Data</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
