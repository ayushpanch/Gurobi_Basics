import streamlit as st

def multiply_numbers(a, b, c, d):
    return a * b * c * d

def main():



    st.title("Multiplication App")

    # Input fields
    num1 = st.number_input("Enter number 1", value=1.0)
    num2 = st.number_input("Enter number 2", value=1.0)
    num3 = st.number_input("Enter number 3", value=1.0)
    num4 = st.number_input("Enter number 4", value=1.0)

    # Compute button
    if st.button("Compute"):
        result = multiply_numbers(num1, num2, num3, num4)
        st.success(f"The result of multiplication is: {result}")

if __name__ == "__main__":
    main()