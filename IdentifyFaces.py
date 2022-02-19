# Yathavi Nandakumar
# Identify all faces in the image by comparing it to known images, then label the known and unknown faces

import face_recognition
from PIL import Image, ImageDraw 

# Get encodings of known images
firstKnownImage = face_recognition.load_image_file('./russell-westbrook.jpg')
firstImageEncoding = face_recognition.face_encodings(firstKnownImage)[0]

secondKnownImage = face_recognition.load_image_file('./kevin-durant.jpg')
secondImageEncoding = face_recognition.face_encodings(secondKnownImage)[0]

thirdKnownImage = face_recognition.load_image_file('./james-harden.jpg')
thirdImageEncoding = face_recognition.face_encodings(thirdKnownImage)[0]

#  Collect all known encodings into an array
knownImageEncodings = [firstImageEncoding, secondImageEncoding, thirdImageEncoding]

# Specify the labels of the known images
knownImageNames = ["Russell Westbrook", "Kevin Durant", "James Harden"]

# Load unlabeled image to identify faces
unlabeledImage = face_recognition.load_image_file('./si-rw-jh-kd.jpg') 

# Find all faces in unlabeled image
faceCoordinates = face_recognition.face_locations(unlabeledImage)
faceEncodings = face_recognition.face_encodings(unlabeledImage, faceCoordinates)

# Convert to PIL so it can be drawn on
pilImage = Image.fromarray(unlabeledImage)
draw = ImageDraw.Draw(pilImage)

# Iterate through all faces
for(top, right, bottom, left), faceEncoding in zip(faceCoordinates, faceEncodings):
  # See if the unlabeled face has a match in the known images
  matches = face_recognition.compare_faces(knownImageEncodings, faceEncoding)

  # Default unknown face labels to "Unknown"
  name = "Unknown"

  # If there's a match
  if True in matches:
    knownImageIndex = matches.index(True) # Get index of matched known image
    name = knownImageNames[knownImageIndex] # Get name of matched image
  
  # Draw box around the face
  draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0)) # Uses the coordinates of the face to draw the box (black outline)

  # Draw the label of the box
  textWidth, textHeight = draw.textsize(name) # Get height and width of the text
  draw.rectangle(((left, bottom - textHeight - 10), (right, bottom)), fill=(0,0,0), outline=(255,255,0)) # Rectangle to put text in
  draw.text((left + 5, bottom - textHeight - 5), name, fill=(255, 255, 255, 255)) # Write the text (white font)

# Delete draw instance to clear up memory
del draw

# Show the labeled image
pilImage.show()

# Save the labeled image
pilImage.save('labeledImage.jpg')
