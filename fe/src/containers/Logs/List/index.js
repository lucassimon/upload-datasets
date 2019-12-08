import React from 'react';
import { Grid, Table } from 'semantic-ui-react';

import Item from './Item';

const List = ({ logs }) => {
  if (logs === null) { return null; }
  return (
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
            {logs.map(item => (<Item key={item.id} log={item} />))}
          </Table.Body>
        </Table>
      </Grid.Column>
    </Grid.Row>
  );
};

List.defaultProps = {};

export default List;
