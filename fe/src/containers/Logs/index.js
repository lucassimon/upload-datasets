import React from 'react';
import { Grid, Table, Pagination } from 'semantic-ui-react';

import LogService from '../../services/LogSetService';
import Item from './Item';


class List extends React.Component {
  state = { logs: [], pages: 1, total: 0, page: 1 }

  componentDidMount() {
    this.fetch(1);
  }

  fetch = async () => {
    const { datasetId } = this.props;
    const { page: actualPage } = this.state;

    try {
      const response = await LogService.listByDatasetId(datasetId, actualPage);
      const {
        data, total, pages, page
      } = response.data;
      this.setState({
        logs: data, total, pages, page
      });
    } catch (error) {
      console.log(error);
    }
  }

  handlePaginationChange = (e, { activePage }) => {
    this.setState({ page: activePage }, () => this.fetch(activePage));
  }

  render() {
    const { logs, pages, page } = this.state;
    if (logs === null) { return null; }
    return (
      <div>
        <Grid.Row>
          <Grid.Column>
            <Table celled>
              <Table.Header>
                <Table.Row>
                  <Table.HeaderCell>Linha</Table.HeaderCell>
                  <Table.HeaderCell>Coluna</Table.HeaderCell>
                  <Table.HeaderCell>Valor</Table.HeaderCell>
                  <Table.HeaderCell>Mensagem</Table.HeaderCell>
                </Table.Row>
              </Table.Header>
              <Table.Body>
                {(logs || []).map((item) => (<Item key={item.id} log={item} />))}
              </Table.Body>
            </Table>
          </Grid.Column>
        </Grid.Row>
        <Grid.Row>
          <Grid.Column size="12">
            <Pagination
              activePage={page}
              onPageChange={this.handlePaginationChange}
              totalPages={pages}
            />
          </Grid.Column>
        </Grid.Row>
      </div>
    );
  }
}

List.defaultProps = {};

export default List;
