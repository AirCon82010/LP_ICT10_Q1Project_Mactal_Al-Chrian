from pyscript import document, display

def create_order(e):
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")

    total = (float(item1.value) * item1.checked +
             float(item2.value) * item2.checked +
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked +
             float(item5.value) * item5.checked)

    customer_name = document.getElementById("customer").value
    customer_address = document.getElementById("address").value
    contact_number = document.getElementById("contact_number").value

    display(f"🏁 Order for: {customer_name}", target="order_output1", append=False)
    display(f"📍 Address: {customer_address}", target="order_output2", append=False)
    display(f"📞 Contact number: {contact_number}", target="order_output3", append=False)
    display(f"💰 Total: ₱ {total:.2f}", target="show", append=False)
