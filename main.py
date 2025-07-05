import gradio as gr

def show_image(image):
    return image

iface = gr.Interface(
    fn=show_image,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Image(type="pil", label="Uploaded Image"),
    title="Simple Image Upload and Display",
    description="Upload an image to see it displayed below."
)

if __name__ == "__main__":
    iface.launch() 