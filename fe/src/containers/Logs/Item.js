import React from 'react';
import { Table, } from 'semantic-ui-react';

const LogItem = ({ log }) => (
  <Table.Row>
    <Table.Cell>{log.row}</Table.Cell>
    <Table.Cell>{log.column}</Table.Cell>
    <Table.Cell>{log.value}</Table.Cell>
    <Table.Cell>{log.message}</Table.Cell>
  </Table.Row>
);

export default LogItem;
