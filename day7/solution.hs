{-# LANGUAGE ScopedTypeVariables #-}

-- %%
import Control.Arrow
import Data.List

-- %{
part1 :: [(Int, Int)] -> Int
part1 pgs = minimum [fuel p pgs | p <- [p'min .. p'max]]
  where
    (p'min, p'max) =
      let (p'min, _) = head pgs
          (p'max, _) = last pgs
       in (p'min, p'max)
    fuel :: Int -> [(Int, Int)] -> Int
    fuel p = go 0
      where
        go :: Int -> [(Int, Int)] -> Int
        go cum [] = cum
        go cum ((op, cnt) : rest) = go (cum + abs (p - op) * cnt) rest

-- %}

-- %{
part2 :: [(Int, Int)] -> Int
part2 pgs = minimum [fuel p pgs | p <- [p'min .. p'max]]
  where
    (p'min, p'max) =
      let (p'min, _) = head pgs
          (p'max, _) = last pgs
       in (p'min, p'max)
    fuel :: Int -> [(Int, Int)] -> Int
    fuel p = go 0
      where
        go :: Int -> [(Int, Int)] -> Int
        go cum [] = cum
        go cum ((op, cnt) : rest) =
          go (cum + (nsteps * (nsteps + 1) `div` 2) * cnt) rest
          where
            nsteps = abs $ p - op

-- %}

main :: IO ()
main = do
  -- %{ -- Parse Input
  ps :: [Int] <-
    fmap read . words
      . fmap
        (\c -> if c == ',' then ' ' else c)
      <$> readFile "day7/input"
  -- %}
  -- %{
  let pgs = (head &&& length) <$> group (sort ps)
  -- %}

  -- %% -- Part 1
  print $ part1 pgs

  -- %% -- Part 2
  print $ part2 pgs
