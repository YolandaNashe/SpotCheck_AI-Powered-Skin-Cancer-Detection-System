from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index_page.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = get_response(user_message)
    return jsonify({'response': response})

def get_response(message):
    message = message.lower()  # Convert message to lowercase for case-insensitive matching

    # Greetings
    if any(word in message for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! Welcome to the Skin Cancer health support chat.How can i assist you today? Do you have any questions, need information on specific topic in regards to skin cancer an all its types?"
    
    elif any(word in message for word in ["how are you", "how is it", "what's up"]):
        return "I am an AI chatbot model, so i dont have feelings or emotions like humans do, but i am fuctioning properly and ready to assist you with any questions regarding skin cancer"

    elif any(word in message for word in ["your creator", "who created you", "where did you come from"]):
        return "I was created by Yolanda Mashlengwe with a sore purpose of assisting anyone who needs to know any information about skin cancer and its types"


    # Goodbyes
    elif any(word in message for word in ["goodbye", "bye", "see you"]):
        return "Goodbye! Have a great day!"

    # Thank you
    elif any(word in message for word in ["thank you", "thanks", "appreciate it"]):
        return "You're welcome! If you have any more questions, feel free to ask."

    # Skin Cancer types Types
    elif any(word in message for word in ["skin cancer type", "types of skin cancer","skin cancer classes","classes of skin cancer"]):
        return "There are seven main types of skin cancer: Melanona, Basal Cell Carsinoma, Actinic Keratoses,Benign keratosis-like lesions,Dermatofibroma,Melanocytic nevi,Vascular lesions. Each has different characteristics affecting the skin."

    # Description for each skin cancer type
    elif any(word in message for word in ["describe", "classify", "description of", "Define","what is"]):
        if "basal cell carsinoma" in message:
            return "Basal Cell Carsinoma (BCC) is the most common type of skin cancer, accounting for about 80% of all skin cancer cases. It originates from basal cells in the epidrmis (outer skin layer) and is usually caused by exposure to UV radiation from the sun or tanning beds."
        elif "melanona" in message:
            return "Melanona is a type of skin cancer that originates from melanocytes, the cells responsible for producing pigment (melanin) in the skin. It is known to be the most aggressive type of skin cancer, accounting for only about 1% of skin cancer cases but responsible for the majority of skin cancer related deaths."
        elif "actinic keratoses" in message:
            return "Actinic keratoses are precancerous lesions that can progress to squamous cell carcinoma (SCC), a type of skin cancer."
        elif "dermatofibroma" in message:
            return "Dermatofibroma are small, non-cancerous skin growths nd they are not a form of skin cancer. However in rare cases a dermatofibroma can resemble a skin cancer."
        elif "melanocytic nevi" in message:
            return "Melanocytic nevi (moles)can potentially develop into skin cancer, specially melanona. while most moles are non-cancerous, some may undergo changes that lead to cancer."
        elif "vascular lession" in message:
            return "Vascular lessions can be benign (non-cancerous) or malignant (cancerous). While most vascular lessions are harmless, some can increase the risk of skin cancer or may be a sign of an underlying cancer."
        elif "benign keratosis_like lesions" in message:
            return "Benign keratosis-like lessions are non-cancerous skin growths that can resemble keratoses, which are rough, scaly patches on the skin."



    # Causes of each skin cancer type
    elif any(word in message for word in ["what are the causes", "cause","causes"]):
        if "basal cell carsinoma" in message:
            return "Exposure to UV radiation from the sun or tanning beds, genetic mutations,weakened immune system, history of cancer, radiation exposure, certain chemicals like arsenic exposure and coal tar and pitch, fair skin."
        elif "melanona" in message:
            return "Exposure to UV radiation from the sun or tanning beds, genetic mutations, and weakened immune systems."
        elif "actinic keratoses" in message:
            return "Prolonged exposure to ultraviolet (UV) radiation from the sun or tanniing beds. Other risk factores include, older age, weakened immune system, history of cancer, genetic predisposition, fair skin"
        elif "dermatofibroma" in message:
            return "The exact cause of dermatofibrosarcoma protuberans(DFSP) is unkown but potential risks are genetic mutations, trauma or injury to the skin, abnormal skin cell growth, immune system dysfunction, family history of DFSP"
        elif "melanocytic nevi" in message:
            return "The exact causes of melanocytic nevi transforming into melanoma are not fully understood, but several factors can increase the risk which are Genetics,UV radiation exposure, Weakened immune system, Dysplastic nevi,Previous melanoma,Hormonal factors, Environmental factors."
        elif "vascular lession" in message:
            return "The causes of vascular lesion skin cancer include, Infections, Chronic inflammation,Injury or trauma to the skin, Aging, Weakened immune systems,Exposure to chemicals like arsenic or pesticides, UV radiation exposure."
        elif "benign keratosis_like lesions" in message:
            return "The causes of benign keratosis-like lesions that can potentially develop into skin cancer include, Human papillomavirus (HPV) infection,Chronic inflammation,Chronic inflammation,Injury or trauma to the skin, Aging, Weakened immune systems,Exposure to chemicals like arsenic or pesticides, UV radiation exposure ."
    

    # Diet and ways to Cope or medication
    elif any(word in message for word in ["how to cope", "diet", "ways to cope", "what to eat", "medication", "lifestyle"]):
       if "basal cell carcinoma" in message:
           diet = ["Increase vitamin D", "calcium", "antioxidants"]
           coping_mechanisms = ["Stress management", "sunscreen protection"]
           medications = ["Topical creams (e.g., imiquimod, fluorouracil)", "Oral medications (e.g., vismodegib, sonidegib)", "Surgery or radiation therapy"]
        
           diet_list = "\n".join([f"{i}. {item}" for i, item in enumerate(diet, start=1)])
           coping_mechanisms_list = "\n".join([f"{i}. {item}" for i, item in enumerate(coping_mechanisms, start=1)])
           medications_list = "\n".join([f"{i}. {item}" for i, item in enumerate(medications, start=1)])
        
           return f"""
           Diet: 
           {diet_list}
           Coping mechanisms: 
           {coping_mechanisms_list}
           Medications: 
           {medications_list}
           """
       elif "melanoma" in message:
           diet = ["Increase omega-3 fatty acids", "vitamin D", "antioxidants"]
           coping_mechanisms = ["Stress management", "support groups"]
           medications = ["Immunotherapy (e.g., ipilimumab, nivolumab)", "Targeted therapy (e.g., vemurafenib, dabrafenib)", "Chemotherapy (e.g., dacarbazine)"]
        
           diet_list = "\n".join([f"{i}. {item}" for i, item in enumerate(diet, start=1)])
           coping_mechanisms_list = "\n".join([f"{i}. {item}" for i, item in enumerate(coping_mechanisms, start=1)])
           medications_list = "\n".join([f"{i}. {item}" for i, item in enumerate(medications, start=1)])
        
           return f"""
           Diet: 
           {diet_list}
           Coping mechanisms: 
           {coping_mechanisms_list}
           Medications: 
           {medications_list}
           """
       
       elif "actinic keratoses" in message:
            return "Prolonged exposure to ultraviolet (UV) radiation from the sun or tanniing beds. Other risk factores include, older age, weakened immune system, history of cancer, genetic predisposition, fair skin"
       elif "dermatofibroma" in message:
            return "The exact cause of dermatofibrosarcoma protuberans(DFSP) is unkown but potential risks are genetic mutations, trauma or injury to the skin, abnormal skin cell growth, immune system dysfunction, family history of DFSP"
       elif "melanocytic nevi" in message:
            return "The exact causes of melanocytic nevi transforming into melanoma are not fully understood, but several factors can increase the risk which are Genetics,UV radiation exposure, Weakened immune system, Dysplastic nevi,Previous melanoma,Hormonal factors, Environmental factors."
       elif "vascular lession" in message:
            return "The causes of vascular lesion skin cancer include, Infections, Chronic inflammation,Injury or trauma to the skin, Aging, Weakened immune systems,Exposure to chemicals like arsenic or pesticides, UV radiation exposure."
       elif "benign keratosis_like lesions" in message:
            return "The causes of benign keratosis-like lesions that can potentially develop into skin cancer include, Human papillomavirus (HPV) infection,Chronic inflammation,Chronic inflammation,Injury or trauma to the skin, Aging, Weakened immune systems,Exposure to chemicals like arsenic or pesticides, UV radiation exposure ."


    # Climate by Soil Type
    elif any(word in message for word in ["climate", "weather"]):
        if "humus" in message:
            return "Humus-rich soil thrives in temperate climates with moderate rainfall, providing ideal conditions for organic matter decomposition."
        elif "sand" in message:
            return "Sandy soil thrives in warm, dry climates with good drainage, allowing roots to access water and nutrients."
        elif "silt" in message:
            return "Silty soil does well in mild climates with moderate rainfall, maintaining good water retention without waterlogging."
        elif "clay" in message:
            return "Clay soil prefers cool, moist climates with adequate drainage to prevent waterlogging and support root growth."
        elif "gravel" in message:
            return "Gravelly soil is adaptable but benefits from well-drained climates that prevent water accumulation around roots."

    # Soil Improvement Tips
    elif any(word in message for word in ["improve soil", "soil improvement", "tips"]):
        if "humus" in message:
            return "To improve humus-rich soil, add compost regularly to enhance nutrient content and soil structure."
        elif "sand" in message:
            return "Improve sandy soil by adding organic matter like compost to increase water retention and nutrient levels."
        elif "silt" in message:
            return "Enhance silty soil by aerating regularly to improve drainage and prevent compaction. Add organic matter for nutrients."
        elif "clay" in message:
            return "Improve clay soil by adding organic amendments like compost to enhance drainage and loosen soil structure."
        elif "gravel" in message:
            return "To improve gravelly soil, focus on improving water retention by adding organic matter and mulching to reduce erosion."

    else:
        return "I'm sorry, I'm not sure about that. Can you please specify your skin cancer-related question?"

if __name__ == "__main__":
    app.run(debug=True)
