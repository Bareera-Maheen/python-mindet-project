# import streamlit as st
# import pandas as pd
# from io import BytesIO

# st.set_page_config(page_title="File Convertor", layout="wide")
# st.title("File Convertor & Cleaner")
# st.write("Upload csv and excel files,clean data , and convert formats." )

# files = st.file_uploader("Upload Csv or Excel file.", type=["csv", "xlsx"])

# if uploaded_files:
#     for file in uploaded_files:
#         if file is not None:  # Check if the file is uploaded
#             ext = file.name.split(".")[-1]  # Get the file extension
#             df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

#         if st.checkbox(f"Remove Dublicates-{file.name}"):
#             df=df.drop_duplicates()
#             st.success("Duplicates Removed")
#             st.dataframes(df.head())

#             if st.checkbox(f"Fill Missing Values - {file.name}"):
#                 df= file (df.select_dtypes(include=["number"]).mean(),inplace=True)
#             st.success("Missing Values filled with mean")
#             st.dataframe(df.head())

#             selected_columns =st.multiselect(f"select columns-{file.name}",df.column, default=df.columns)
#             df= df(selected_columns)
#             st.dataframes(df.head())

#             if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
#              st.bar_chart(df.select_datatypes(include="number").iloc[:,:2])

#             format_choise=st.radio_chart(f"Convert {file.name} to:",["csv","excel"],key=file.name)

#             if st.button(f"Download {file.name} as {format_choise}") :
#                 output = BytesIO
#                 if format_choise=="csv":
#                     df.to_csv(output,index=False)
#                     mine = "text/csv" 
#                     new_name=file.name.replace(ext ,".csv")

#                 else:
#                     df.to_excel(output, index=False , engine='openpyxl')
#                     mine = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                     new_name = file.name.replace(ext, "xlsx")
#                 output.seek(0)
#                 st.set_download_button(new_name, data=output, minetype=mine)
#                 st.success("processing complete!")



import streamlit as st
import pandas as pd
from io import BytesIO

# Page configuration
st.set_page_config(page_title="File Convertor", layout="wide")
st.title("File Convertor & Cleaner")
st.write("Upload CSV and Excel files, clean data, and convert formats.")

# File uploader
uploaded_files = st.file_uploader("Upload CSV or Excel file.", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        if file is not None:  # Check if the file is uploaded
            ext = file.name.split(".")[-1]  # Get the file extension
            df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
            
            st.subheader(f"{file.name} - Preview")
            st.dataframe(df.head())

            # Remove duplicates
            if st.checkbox(f"Remove Duplicates - {file.name}"):
                df = df.drop_duplicates()
                st.success("Duplicates Removed!")
                st.dataframe(df.head())

            # Fill missing values
            if st.checkbox(f"Fill Missing Values - {file.name}"):
                df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
                st.success("Missing Values Filled with Mean!")
                st.dataframe(df.head())

            # Select columns
            selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
            df = df[selected_columns]
            st.dataframe(df.head())

            # Show chart
            if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            # Convert file format
            format_choice = st.radio(f"Convert {file.name} to:", ["csv", "excel"], key=file.name)

            if st.button(f"Download {file.name} as {format_choice}"):
                output = BytesIO()
                if format_choice == "csv":
                    df.to_csv(output, index=False)
                    mime = "text/csv"
                    new_name = file.name.replace(ext, ".csv")
                else:
                    df.to_excel(output, index=False, engine="openpyxl")
                    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    new_name = file.name.replace(ext, ".xlsx")
                
                output.seek(0)
                st.download_button(label=f"Download {new_name}", data=output, file_name=new_name, mime=mime)
                st.success("Processing Complete!")