import frappe
from frappe.model.document import Document

class NutritionProfile(Document):
    def before_save(self):
        self.calculate_nutritional_needs()

    def calculate_nutritional_needs(self):
        # Example logic for calculating nutritional needs
        if self.age and self.weight and self.height:
            self.calories = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + (5 if self.gender == 'Male' else -161)
        else:
            frappe.throw("Age, weight, height, and gender are required to calculate BMR (Basal Metabolic Rate).")