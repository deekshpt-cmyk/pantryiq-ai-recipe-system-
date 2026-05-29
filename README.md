# 🍳 PantryIQ - AI Recipe System

An intelligent kitchen assistant powered by computer vision and AI that detects ingredients from images and recommends recipes in real-time. Built with YOLOv8, Streamlit, and OpenAI.

## ✨ Features

- **🔍 Real-time Ingredient Detection**: Uses YOLOv8 computer vision to identify ingredients from images
- **🍲 Smart Recipe Recommendations**: AI-powered recipe engine that suggests dishes based on detected ingredients
- **💬 Gen-Z Chatbot**: Interactive chatbot interface with personality-driven responses
- **📱 Streamlit UI**: Beautiful, responsive web interface with custom styling
- **🤖 OpenAI Integration**: Leverages GPT for intelligent recommendations and interactions

## 🎯 Use Cases

- Quickly find recipes based on ingredients you have
- Reduce food waste by discovering uses for leftover ingredients
- Get personalized recipe suggestions with an AI chatbot
- Learn about nutritional information and cooking tips

## 🛠️ Tech Stack

- **Backend**: Python, OpenAI API
- **Computer Vision**: YOLOv8 (Object Detection)
- **Frontend**: Streamlit
- **Image Processing**: OpenCV, Pillow
- **ML Library**: Scikit-learn
- **Environment Management**: python-dotenv

## 📋 Requirements

```
streamlit==1.37.0
ultralytics==8.0.0
opencv-python==4.8.0.74
opencv-contrib-python==4.8.0.74
Pillow==10.0.0
scikit-learn==1.3.0
openai==1.0.0
python-dotenv==1.0.0
```

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pantryiq-ai-recipe-system.git
cd pantryiq-ai-recipe-system
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Add your OpenAI API key to .env
```

## 💻 Usage

### Run the Main Application
```bash
streamlit run app.py
```

### Run the Mise App (Alternative UI)
```bash
streamlit run ui/mise_app.py
```

## 📁 Project Structure

```
pantryiq-ai-recipe-system/
├── app.py                 # Main Streamlit application
├── chatbot.py            # Gen-Z chatbot module
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
│
├── ai/                   # AI & ML modules
│   ├── detect.py         # YOLOv8 ingredient detection
│   ├── recipe_engine.py  # Recipe recommendation engine
│   ├── yolov8n.pt        # YOLOv8 pretrained model
│   └── __init__.py
│
├── ui/                   # User Interface components
│   └── mise_app.py       # Alternative Streamlit UI (Mise)
│
├── data/                 # Data files
│   └── recipes.json      # Recipe database
│
└── README.md            # This file
```

## 🎬 How It Works

1. **Upload an Image**: Use the Streamlit UI to upload a photo of your ingredients
2. **Detection**: YOLOv8 analyzes the image and identifies ingredients
3. **Recommendation**: The recipe engine searches available recipes matching detected ingredients
4. **Chat**: Interact with the Gen-Z chatbot to get cooking tips and personalized suggestions

## 🔑 Key Modules

### `ai/detect.py`
- Loads YOLOv8 model
- Processes input images
- Returns detected ingredients with confidence scores

### `ai/recipe_engine.py`
- Matches detected ingredients to recipes
- Ranks recipes by ingredient overlap
- Returns top recommendations

### `chatbot.py`
- Personality-driven responses
- Integration with OpenAI API
- Context-aware cooking suggestions

### `app.py`
- Main Streamlit interface
- Handles image uploads and processing
- Displays results with custom styling

## 🎨 Features Highlights

- **Custom Styling**: Beautiful sage-green gradient UI with modern typography
- **Real-time Processing**: Fast ingredient detection and recipe matching
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Error Handling**: Robust error management for API calls and model inference

## � Screenshots & Results

### Application Interface
The Mise AI Kitchen Intelligence interface with ingredient detection and chatbot:

![PantryIQ Application](temp.jpg)

### System Output Example

**Input**: Upload an image with ingredients
```
User uploads: Photo with tomato, lettuce, onion, garlic, and basil
```

**Detection Output**:
```
🔍 Detected Ingredients (with confidence scores):
  • Tomato: 98.5%
  • Lettuce: 96.2%
  • Onion: 94.8%
  • Garlic: 92.1%
  • Basil: 89.7%
```

**Recipe Recommendations**:
```
🍲 Top Recipe Matches:
  1. Italian Bruschetta (Match: 85%)
  2. Fresh Garden Salad (Match: 78%)
  3. Tomato Soup (Match: 81%)
  4. Italian Pasta (Match: 72%)
```

**Chatbot Response** (Gen-Z style):
```
"Yo! 🔥 With those fresh ingredients you can literally make the most fire 
Italian dishes! Bruschetta would hit different right now, fr fr. You could 
also go for a fresh salad or creamy tomato soup - no cap! 💯"
```

## 🔧 Configuration

Edit `.env` file to configure:
```
OPENAI_API_KEY=your_api_key_here
```

## 🚀 Future Enhancements

- [ ] Nutritional information display
- [ ] Dietary restriction filtering
- [ ] Shopping list generation
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] User recipe history/favorites


## 👨‍💼 Author

Created as an AI recipe recommendation system showcasing:
- Computer vision implementation
- Real-time API integration
- Full-stack web application development
- ML model deployment

---

