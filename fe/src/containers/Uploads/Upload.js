import React, { Component } from 'react';

import Dropzone from 'react-dropzone';
import { Grid, Form, Image } from 'semantic-ui-react';

class Upload extends Component {
  renderDragMessage = (isDragActive, isDragReject) => {
    if (!isDragActive) {
      return 'Arraste arquivos aqui';
    }

    if (isDragReject) {
      return 'Arquivo não suportado';
    }

    return 'Solte os arquivos aqui';
  }

  render() {
    const { onUpload } = this.props;
    console.log(onUpload)
    return (
      <Dropzone
        onDropAccepted={onUpload}
      >
        { ({
          getRootProps,
          getInputProps,
          isDragActive,
          isDragReject,
        }) => {
          return (
            <Grid centered>
              <Grid.Row>
                <Grid.Column width="12">
                  <Form.Field>
                    <Image
                      src="https://react.semantic-ui.com/images/wireframe/image.png"
                      size="tiny"
                      bordered
                      {...getRootProps()}
                    />
                    <p>{ this.renderDragMessage(isDragActive, isDragReject) }</p>
                    <input {...getInputProps()} />
                  </Form.Field>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          );
        }}
      </Dropzone>
    );
  }
}

export default Upload;
