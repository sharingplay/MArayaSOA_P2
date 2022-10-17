import google.auth, io
from google.cloud import vision

credentials, project = google.auth.default()



def analyze_emotion():
    client = vision.ImageAnnotatorClient()
    image_path = f'.\sad.jpg'
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    #image = vision.Image(content=image_bytes)
    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    #respuesta del sentimiento
    face_annotation = response.face_annotations
    # Toma solo la primera cara
    analist = face_annotation[0]
    #Compara el resultado para cada sentimiento
    #El estado varia de 0 a 5
    answer = ["no se sabe"]
    if (analist.detection_confidence >= 4) and (analist.detection_confidence <= 5):
        answer += ["confiado"]
    if (analist.anger_likelihood >= 4) and (analist.anger_likelihood <= 5):
        answer += ["enojado"]
    if (analist.joy_likelihood >= 4) and (analist.joy_likelihood <= 5):
        answer += ["muy feliz"]
    if (analist.sorrow_likelihood >= 4) and (analist.sorrow_likelihood <= 5):
        answer += ["triste"]
    if (analist.surprise_likelihood >= 4) and (analist.surprise_likelihood <= 5):
        answer += ["sorprendido"]
    #Separa todos los estados de la personas
    resp = ''
    if len(answer) == 1:
        resp = answer[0]
    else:
        for person in answer:
            if person != "no se sabe":
                resp += person + ", "
    print(resp)
    return resp

analyze_emotion()