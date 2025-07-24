# import streamlit as st
# import langchain_helper
#
# st.title("Restaurant Name Generator")
#
# cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))
#
# if cuisine:
#     response = langchain_helper.generate_restaurant_name_and_items(cuisine)
#     st.header(response['restaurant_name'].strip())
#     menu_items = response['menu_items'].strip().split(",")
#     st.write("**Menu Items**")
#     for item in menu_items:
#         st.write("-", item)
import streamlit as st
import langchain_helper

st.title("🍽️ Restaurant Name Generator")

# Sidebar to pick cuisine
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

# Generate and display results
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    # Display restaurant name
    st.header(f"🏠 {response['restaurant_name'].strip()}")

    # Process and display menu items
    raw_items = response['menu_items']
    menu_items = [item.strip() for item in raw_items.strip().split(",") if item.strip()]

    st.subheader("🍴 Menu Items:")
    for item in menu_items:
        st.write(f"- {item}")

