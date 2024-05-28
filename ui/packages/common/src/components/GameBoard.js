import React, { useState } from 'react';
import styled from 'styled-components';

const BoardContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 100px);
  grid-gap: 10px;
  margin: 20px auto;
  max-width: 320px;
`;

const Cell = styled.div`
  width: 100px;
  height: 100px;
  background: #fff;
  border: 1px solid #333;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  cursor: pointer;
`;

const GameBoard = () => {
  const [board, setBoard] = useState(Array(9).fill(null));

  const handleClick = (index) => {
    const newBoard = [...board];
    newBoard[index] = 'X';
    setBoard(newBoard);
  };

  return (
    <BoardContainer>
      {board.map((cell, index) => (
        <Cell key={index} onClick={() => handleClick(index)}>
          {cell}
        </Cell>
      ))}
    </BoardContainer>
  );
};

export default GameBoard;
