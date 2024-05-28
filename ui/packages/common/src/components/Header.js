import React from 'react';
import { View, Text } from 'react-native';
import { Link } from 'react-router-dom';
import styled from 'styled-components/native';

const HeaderContainer = styled.View`
  background: #333;
  color: #fff;
  padding: 10px;
  text-align: center;
`;

const HeaderText = styled.Text`
  color: #fff;
  margin: 0 10px;
  text-decoration: none;
`;

const Header = () => (
  <HeaderContainer>
    <HeaderText>Game App</HeaderText>
    <View>
      <Link to="/"><HeaderText>Home</HeaderText></Link>
      <Link to="/game"><HeaderText>Game</HeaderText></Link>
      <Link to="/about"><HeaderText>About</HeaderText></Link>
    </View>
  </HeaderContainer>
);

export default Header;
