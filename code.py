import streamlit as st

def main():
    st.title("Simple User Information Form")

    name = st.text_input("Enter your name")
    gmail = st.text_input("Enter your Gmail address")
    message = st.text_area("Enter your message")

    if st.button("Submit"):
        st.write("## Submitted Information")
        st.write(f"**Name:** {name}")
        st.write(f"**Gmail:** {gmail}")
        st.write(f"**Message:** {message}")

if __name__ == "__main__":
    main()
