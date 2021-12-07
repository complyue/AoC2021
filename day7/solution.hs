{-# LANGUAGE ScopedTypeVariables #-}

-- %%
import Control.Arrow
import Data.List

-- %{
minFuel :: [(Int, Int)] -> (Int -> Int) -> Int
minFuel pgs formula = minimum [fuel p pgs | p <- [p'min .. p'max]]
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
          go (cum + formula (abs (p - op)) * cnt) rest

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
  print $ minFuel pgs id

  -- %% -- Part 2
  print $ minFuel pgs $ \nsteps -> nsteps * (nsteps + 1) `div` 2
