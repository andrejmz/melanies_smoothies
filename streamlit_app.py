# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Example Streamlit App :cup_with_straw:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)



title = st.text_input('Name on smoothie')
st.write('the name on your smoothie will be:', title)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))

editable_df = st.experimental_data_editor(my_dataframe)

ingredients_list = st.multiselect('Choose up to 5', my_dataframe);

if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)
    ingredients_string = ''
    for chosen_fruit in ingredients_list:
        ingredients_string += chosen_fruit + ' '
        st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
    values ('""" + ingredients_string + """','""" + title +"""')"""
    time_to_insert = st.button('Submit order')
    st.write(my_insert_stmt)

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

#st.dataframe(data=my_dataframe, use_container_width=True)