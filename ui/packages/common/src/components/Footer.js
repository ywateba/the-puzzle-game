import React from 'react';
import styled from 'styled-components';

const FooterContainer = styled.footer`
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
  margin-top: auto;
`;

const Footer = () => (
  <FooterContainer>
    <p>&copy; 2024 Game App. All rights reserved.</p>
  </FooterContainer>
);

export default Footer;
