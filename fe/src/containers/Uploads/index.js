import React from 'react';
import axios from 'axios';
import { OrderedMap } from 'immutable';
import { uuid } from 'uuidv4';
import filesize from 'filesize';
import slugify from 'slugify';
import {
  Container, Grid, Select
} from 'semantic-ui-react';

import Upload from './Upload';


const calculateProgress = (evt) => (
  parseInt(Math.round((evt.loaded * 100) / evt.total), 10));

const getPayloadData = (file, kind) => {
  const data = new FormData();
  data.append('dataset_file', file.file, file.name);
  data.append('kind', kind);
  return data;
};

const getFilesMap = (acceptedFiles) => (
  OrderedMap(acceptedFiles.map((file) => {
    const id = uuid();
    const data = {
      file,
      id,
      name: slugify(file.name.toLowerCase()),
      readableSize: filesize(file.size),
      preview: URL.createObjectURL(file),
      progress: 0,
      uploaded: false,
      error: false,
      url: null,
    };
    return [id, data];
  })));

class Create extends React.Component {
  state = { files: OrderedMap(), kind: '' }

  componentDidMount() {}

  componentWillUnmount() {
    const { files } = this.state;
    files.valueSeq().toArray().forEach((file) => URL.revokeObjectURL(file.preview));
  }

  handleUpload = (handleFiles) => {
    const uploadedFiles = getFilesMap(handleFiles);

    this.setState(
      ({ files }) => ({ files: files.merge(uploadedFiles) }),
      () => {
        uploadedFiles.valueSeq().toArray().forEach(this.processUpload);
      },
    );
  }

  processUpload = (uploadedFile) => {
    const { kind } = this.state;
    const onUploadProgress = (e) => {
      this.setState(
        ({ files }) => ({
          files: files.update(
            uploadedFile.id, state => ({ ...state, progress: calculateProgress(e) }),
          ),
        }),
      );
    };

    const onUploadDone = (response) => {
      const { history: { push } } = this.props;
      push('/datasets/page/1');
    };

    const onUploadError = () => {
      this.setState(
        ({ files }) => ({
          files: files.update(uploadedFile.id, state => ({ ...state, error: true })),
        }),
      );
    };

    console.log(kind);
    axios.post(
      'http://localhost:5000/upload',
      getPayloadData(uploadedFile, kind),
      { onUploadProgress }
    ).then(onUploadDone).catch(onUploadError);
  }

  handleChange = (ev, data) => {
    this.setState({ kind: data.value });
  }

  render() {
    const { kind } = this.state;
    const options = [
      { key: ' ', value: ' ', text: 'Selecione uma opção' },
      { key: 'example', value: 'example', text: 'Exemplo' },
      { key: 'boleto', value: 'boleto', text: 'Boleto' },
      { key: 'caers', value: 'caers', text: 'Caers' },
    ];
    return (
      <Container style={{ marginTop: '7em' }}>
        <Grid>
          <Grid.Row>
            <Select
              placeholder="Selecione o tipo"
              options={options}
              onChange={this.handleChange}
            />
          </Grid.Row>
          <Grid.Row>
            {kind && <Upload onUpload={this.handleUpload} /> }
          </Grid.Row>
        </Grid>
      </Container>
    );
  }
}


export default Create;
