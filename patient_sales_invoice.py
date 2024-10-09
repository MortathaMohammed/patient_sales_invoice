import frappe


def create_sales_invoice_on_patient_creation(doc, method):
    customer_name = create_customer_for_patient(doc)
    
    si = frappe.new_doc("Sales Invoice")
    si.customer = customer_name
    si.due_date = frappe.utils.nowdate()
    
    si.append("items", {
        "item_code": "inpatient service",
        "qty": 1,
        "rate": 0.00 
    })
    
    si.insert()
    # si.submit()

def create_customer_for_patient(patient):
    customer_name = patient.patient_name
    existing_customer = frappe.db.get_value("Customer", {"customer_name": customer_name})
    if existing_customer:
        return existing_customer
    else:
        customer = frappe.new_doc("Customer")
        customer.customer_name = customer_name
        customer.customer_group = "Individual" 
        customer.territory = "All Territories" 
        customer.customer_type = "Individual"
        customer.save()
        return customer.name