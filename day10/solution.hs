{-# LANGUAGE ScopedTypeVariables #-}

-- %%

import Control.Exception
import Data.List
import Data.Maybe

-- %{
validate1 :: String -> Int
validate1 line = go line []
  where
    go :: [Char] -> [Char] -> Int
    go [] _ = 0
    go (next : rest) stack = match next stack $ go rest

    match :: Char -> [Char] -> ([Char] -> Int) -> Int
    match ')' ('(' : stack') k = k stack'
    match ']' ('[' : stack') k = k stack'
    match '}' ('{' : stack') k = k stack'
    match '>' ('<' : stack') k = k stack'
    match ')' _ _k = 3
    match ']' _ _k = 57
    match '}' _ _k = 1197
    match '>' _ _k = 25137
    match c stack k = k $ c : stack

-- %}

-- %{
validate2 :: String -> Maybe Int
validate2 line = go line []
  where
    score :: Int -> [Char] -> Int
    score n [] = n
    score n ('(' : rest) = score (n * 5 + 1) rest
    score n ('[' : rest) = score (n * 5 + 2) rest
    score n ('{' : rest) = score (n * 5 + 3) rest
    score n ('<' : rest) = score (n * 5 + 4) rest
    score _ _ = error "malformed input"

    go :: [Char] -> [Char] -> Maybe Int
    go [] stack = Just $ score 0 stack
    go (next : rest) stack = match next stack $ go rest

    match :: Char -> [Char] -> ([Char] -> Maybe Int) -> Maybe Int
    match ')' ('(' : stack') k = k stack'
    match ']' ('[' : stack') k = k stack'
    match '}' ('{' : stack') k = k stack'
    match '>' ('<' : stack') k = k stack'
    match ')' _ _k = Nothing
    match ']' _ _k = Nothing
    match '}' _ _k = Nothing
    match '>' _ _k = Nothing
    match c stack k = k $ c : stack

-- %}

main :: IO ()
main = do
  -- %{ -- Parse Input
  ls :: [String] <- lines <$> readFile "day10/input"
  -- %}

  -- %% -- Part 1
  print $ sum $ validate1 <$> ls

  -- %% -- Part 2
  let scores = catMaybes $ validate2 <$> ls
  print $ sort scores !! (length scores `div` 2)
