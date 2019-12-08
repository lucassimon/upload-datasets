import React from 'react';
import { Item, Segment, Grid, } from 'semantic-ui-react';

import DatasetItem from './Item';

const List = ({ datasets, handleFetch }) => {
  if (datasets.length === 0) { return null; }
  return (
    <Grid.Row>
      <Grid.Column>
        <Segment padded="very">
          <Item.Group divided>
            {datasets.map(item => <DatasetItem key={item.id} dataset={item} handleFetch={handleFetch} />)}
          </Item.Group>
        </Segment>
      </Grid.Column>
    </Grid.Row>
  );
};

List.defaultProps = { datasets: [] };

export default List;
