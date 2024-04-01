from flask import Flask, request, jsonify
import tensorflow.compat.v1 as tf
import gpt_2_simple as gpt2

# Initialize Flask app
app = Flask(__name__)

# Define route for generating text
@app.route('/generate', methods=['POST'])
def generate_text():
    # Get prompt from request
    prompt = request.json.get('prompt')

    try:
        # Initialize TensorFlow session within the route handler
        with tf.Session() as sess:
            # Load the pre-trained GPT-2 model
            gpt2.load_gpt2(sess, model_name="124M")
            
            # Generate text using GPT-2
            generated_text = gpt2.generate(sess=sess, model_name="124M", prefix=prompt, return_as_list=True)[0]
            
            return jsonify({'generated_text': generated_text})
    except Exception as e:
        # Handle any exceptions that occur during text generation
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
