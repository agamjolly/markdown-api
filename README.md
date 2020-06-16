# Markdown API
A RESTful API written in Flask that converts Markdown into HTML compatible to be used with Pandoc and most CSS libraries.

## Idea
This API would convert all `POST`ed markdown code into basic HTML with no CSS styling. 

- A `POST` request to the API would ensure that the data is sent to the backend server with the appropriate Markdown code. 

- This `POST` request would be returned with compressed HTML code.

## Checklist

- [ ] Work on the converter on CLI
- [ ] Compress markdown and work on unique div classes
- [ ] Handling line breaks
