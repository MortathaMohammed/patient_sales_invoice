
# **Automate Sales Invoice Creation on Patient Registration**

This script automates the creation of a **Sales Invoice** whenever a new **Patient** is registered in ERPNext Healthcare.

## **Overview**

- **Purpose**: Streamline the billing process by automatically generating a Sales Invoice upon patient registration.
- **Scope**: Works specifically with the **Patient** DocType in ERPNext Healthcare.

## **Installation and Setup**

### **1. Add the Script to Your Custom App**

Place the script in your custom app, for example, in a file named `patient_sales_invoice.py`.


### **2. Update `hooks.py`**

In your custom app's `hooks.py` file, add the following to link the script to the Patient DocType:

```python
doc_events = {
    "Patient": {
        "after_insert": "your_app_name.patient_sales_invoice.create_sales_invoice_on_patient_creation"
    }
}
```

- Replace `your_app_name` with the actual name of your custom app.
- Ensure the path `patient_sales_invoice.create_sales_invoice_on_patient_creation` matches the location of your script.

### **3. Restart Bench**

After saving the changes, restart the bench to apply them:

```bash
bench restart
```

## **Configuration**

- **Item Code**: Make sure the item code `"inpatient service"` exists in your Items list or replace it with an existing item code.
- **Rate**: Adjust the `rate` value in the script to reflect the actual price for the service.
- **Customer Details**: Modify `customer_group`, `territory`, and other customer fields as needed.

## **Usage**

- **Create a New Patient**: Go to **Healthcare > Patient** and create a new Patient record.
- **Automatic Invoice Creation**: Upon saving, the script will automatically:
  - Create a corresponding Customer if one doesn't exist.
  - Generate a Sales Invoice linked to the Customer.

## **Notes**

- **Auto-Submit Invoices**: If you want the Sales Invoice to be automatically submitted, uncomment the line `# si.submit()` in the script.
- **Error Handling**: For production use, consider adding try-except blocks to handle potential errors gracefully.
- **Permissions**: Ensure that users have the necessary permissions to create Customers and Sales Invoices.
- **Testing**: Test the script in a development environment before deploying it to production.

## **License**

This script is provided under the MIT License.

---

This `README.md` provides a straightforward guide on how to implement and use the script to automate Sales Invoice creation upon Patient registration in ERPNext Healthcare.