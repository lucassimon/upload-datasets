import React from 'react';
import { withRouter, Link } from 'react-router-dom';
import { Item } from 'semantic-ui-react';

export const DatasetItem = ({ dataset }) => (
  <Item>
    <Item.Content verticalAlign="middle">
      <Item.Header>
        <Link to={`/datasets/${dataset.id}`}>
          {dataset.filename}
        </Link>
      </Item.Header>
    </Item.Content>
  </Item>
);

export default withRouter(DatasetItem);
