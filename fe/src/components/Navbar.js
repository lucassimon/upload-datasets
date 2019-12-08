import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import {
  Container,
  Menu,
} from 'semantic-ui-react';


export const Navbar = () => (
  <Menu attached="top" color="teal" inverted>
    <Container>
      <Menu.Item as={Link} to="/" header>Dashboard</Menu.Item>
      <Menu.Item as={Link} to="/datasets/page/1">Datasets</Menu.Item>
    </Container>
  </Menu>
);

const mapStateToProps = () => ({});

const mapDispatchToProps = () => ({});

const ConnectNavbar = connect(mapStateToProps, mapDispatchToProps)(Navbar);

export default ConnectNavbar;
