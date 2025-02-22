from openai import OpenAI
from typing import List, Dict
from config import OPENAI_API_KEY

class LicenseAnalyzer:
    def __init__(self):
        self.common_licenses = [
            "MIT", "GPL-3.0", "Apache-2.0", "BSD-3-Clause", 
            "LGPL-3.0", "MPL-2.0", "AGPL-3.0"
        ]
        # Initialize OpenAI client with API key
        self.client = OpenAI(api_key=OPENAI_API_KEY)
    
    def analyze_license(self, license_name: str) -> Dict:
        """Analyze a specific license and return its details"""
        prompt = f"""
            Analyze the {license_name} software license and provide:
            1. Brief Summary: A concise explanation of the license.
            2. Permissions: What the license allows (e.g., commercial use, modifications, sublicensing).
            3. Restrictions: What the license prohibits (e.g., attribution requirements, copyleft clauses).
            4. Compliance Requirements: Steps necessary to comply with the license.
            5. Use Case Suitability: Where this license is best applied.

            Format the response in markdown. If the license is not recognized, return: "License not found."
            """
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    def compare_licenses(self, license1: str, license2: str) -> str:
        """Compare two licenses and highlight key differences"""

        prompt = f"""Compare the following two software licenses: **{license1}** vs **{license2}**.
            Provide a side-by-side breakdown covering:
            - Summary: A one-liner summary of each license.
            - Key Permissions: What users can do under each license.
            - Key Restrictions: What users must avoid or comply with.
            - Best Fit Use Cases: When to choose each license.
            - Legal Considerations: Any important legal obligations.

            Ensure the response is formatted in markdown tables for clarity."""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    def analyze_uploaded_license(self, text: str) -> str:
        """Analyze custom license text"""
        prompt = f"""
        Analyze the uploaded software license document and extract:
        1. License Name (if identifiable)
        2. Key Permissions
        3. Restrictions
        4. Compliance Requirements
        5. Any ambiguities or areas needing legal interpretation

        License text:
        {text}
        
        Format the response in markdown."""
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    def get_general_guidance(self, question: str) -> str:
        """Provide guidance for general licensing questions"""

        prompt = f"""
            Provide a clear, accurate, and concise response to the following software licensing question:

            **Question:** {question}

            Ensure the response includes:
            1. A direct answer to the question.
            2. Relevant examples or references(if applicable).
            3. Legal or compliance considerations (if necessary).
            4. Actionable recommendations (if applicable).

            Format the response in markdown for readability.
        """


        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content 