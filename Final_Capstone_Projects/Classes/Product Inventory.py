from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow, QComboBox, QHBoxLayout
from PyQt5.Qt import QLineEdit
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # Initialize UI
        self.init_ui()
        self.setWindowTitle('Inventory Manager')

        # Initiate Inventory
        self.inventory = Inventory()

        self.show()

    def init_ui(self):
        # Create main layout
        main_layout = QVBoxLayout()

        label_1 = QLabel('Current Products')
        self.dropdown = QComboBox()
        self.dropdown.setEditText('Please select a Product')

        # Create buttons
        add_button = QPushButton("Add")
        delete_button = QPushButton("Delete")
        update_button = QPushButton('Update')
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(update_button)

        # Create main product layout
        product_layout = QHBoxLayout()

        # Layout for product labels
        p_labels_layout = QVBoxLayout()
        p_name_label = QLabel('Name:')
        p_price_label = QLabel('Price:')
        p_id_label = QLabel('Id:')
        p_quantity_label = QLabel('Quantity:')
        p_labels_layout.addWidget(p_name_label)
        p_labels_layout.addWidget(p_price_label)
        p_labels_layout.addWidget(p_id_label)
        p_labels_layout.addWidget(p_quantity_label)

        # Layout for product line edits
        p_edit_layout = QVBoxLayout()
        p_price = QLineEdit()
        p_id = QLineEdit()
        p_quantity = QLineEdit()
        p_name = QLineEdit()
        p_name.setPlaceholderText('Enter an String')
        p_price.setPlaceholderText('Enter an Integer')
        p_id.setPlaceholderText('Enter an Integer')
        p_quantity.setPlaceholderText('Enter an Integer')
        p_edit_layout.addWidget(p_name)
        p_edit_layout.addWidget(p_price)
        p_edit_layout.addWidget(p_id)
        p_edit_layout.addWidget(p_quantity)

        # Add product label and edit to main product layout
        product_layout.addLayout(p_labels_layout)
        product_layout.addLayout(p_edit_layout)

        # Check if labels are correct type
        check_inputs = lambda: self.correct_inputs(p_name.text(), p_price.text(), p_id.text(), p_quantity.text())
        update_inputs = lambda: self.update_product(p_name.text(), p_price.text(), p_id.text(), p_quantity.text())

        # Set button functions
        add_button.released.connect(check_inputs)
        update_button.released.connect(update_inputs)
        delete_button.released.connect(self.delete_product)

        main_layout.addWidget(label_1)
        main_layout.addWidget(self.dropdown)
        main_layout.addLayout(product_layout)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def delete_product(self):
        selected_item = self.dropdown.currentIndex()
        self.dropdown.removeItem(selected_item)
        self.inventory.delete_product(self.dropdown.itemText(selected_item))
        print('deleted product')

    def correct_inputs(self, name, price, id, quantity):
        if price.isdigit() and id.isdigit() and quantity.isdigit():
            self.inventory.create_product(name, price, id, quantity)
            self.dropdown.addItem(name)

    def update_product(self, name, price, id, quantity):
        if price.isdigit() and id.isdigit() and quantity.isdigit():
            old_name = self.dropdown.itemText(self.dropdown.currentIndex())
            self.inventory.update_product(old_name, name, price, id, quantity)


class Product(object):
    name = None
    price = -1
    id = -1
    quantity = -1

    def __init__(self, name, price, id, quantity):
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity

    def update_properties(self, name, price, id, quantity):
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity
        print('updated properties')


class Inventory(object):
    products = []

    def update_product(self, old_name, name, price, id, quantity):
        product_names = [p.name for p in self.products]
        self.products[product_names.index(old_name)].update_properties(name, price, id, quantity)
        print('updated product')

    def create_product(self, name, price, id, quantity):
        product_names = [p.name for p in self.products]
        if name not in product_names:
            product = Product(name, price, id, quantity)
            self.products.append(product)
            print('added product')

    def delete_product(self, name):
        for i, p in enumerate(self.products):
            if p.name == name:
                del self.products[i]

# Create application
app = QApplication(sys.argv)
# Open window
window = MainWindow()
# Wait for window to close
sys.exit(app.exec())
