import React from 'react';

import { connect } from 'react-redux';
import { Container, Grid, Pagination } from 'semantic-ui-react';

import DataSetService from '../../../services/DataSetService';

import List from './List';


export class Datasets extends React.Component {
  state = { datasets: null, pages: 1 };

  componentDidMount() { this.fetch(); }

  componentDidUpdate(nextProps) {
    const { match: { params: { pageId } } } = this.props;
    if (nextProps.match.params.pageId !== pageId) {
      this.fetch();
    }
  }

  handlePaginationChange = (e, { activePage }) => {
    const { history: { push } } = this.props;
    push(`/datasets/page/${activePage}`);
  }

  fetch = async () => {
    const { match: { params: { pageId } } } = this.props;
    try {
      const response = await DataSetService.paginated(pageId);
      const { data, pages } = response.data;
      this.setState({ datasets: data, pages });

    } catch (error) {
      console.log(error);
    }
  }

  render() {
    const { datasets, pages } = this.state;
    const { match: { params: { pageId } } } = this.props;
    return (
      <div style={{ marginTop: '7em' }}>
        <Container>
          <Grid>
            {datasets && datasets.length > 0 ? (
              <List datasets={datasets} handleFetch={this.fetch} />
            ) : null }
            <Grid.Row>
              <Grid.Column size="12">
                <Pagination
                  activePage={pageId}
                  onPageChange={this.handlePaginationChange}
                  totalPages={pages}
                />
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </div>
    );
  }
}
const mapStateToProps = () => ({});

const mapDispatchToProps = () => ({});

const ConnectDatasets = connect(mapStateToProps, mapDispatchToProps)(Datasets);

export default ConnectDatasets;
