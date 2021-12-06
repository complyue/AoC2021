{-# LANGUAGE ScopedTypeVariables #-}

-- %%
-- %:set -package array

import Control.Exception
import Data.Array

-- %{
simulate :: Int -> [Int] -> Int
simulate ndays0 timers =
  let (pace'groups, pg7, pg8) = iter ndays0 (pace'groups0, 0, 0)
   in sum pace'groups + pg7 + pg8
  where
    iter :: Int -> (Array Int Int, Int, Int) -> (Array Int Int, Int, Int)
    iter 0 st = st
    iter ndays (pace'groups, pg7, pg8) =
      assert (ndays >= 1) $
        iter (ndays - 1) (pace'groups', pg7', pg8')
      where
        pg0to6 = pace'groups ! 0
        pg7' = pg8
        pg8' = pg0to6
        pace'groups' =
          ixmap
            (0, 6)
            (\i -> if i >= 6 then 0 else i + 1)
            $ pace'groups // [(0, pg0to6 + pg7)]

    pace'groups0 = go timers (array (0, 6) [(i, 0) | i <- [0 .. 6]])
      where
        go :: [Int] -> Array Int Int -> Array Int Int
        go [] a = a
        go (t : rest) a = go rest $ a // [(t, a ! t + 1)]

-- %}

main :: IO ()
main = do
  -- %{ -- Parse Input
  timers :: [Int] <-
    fmap read . words
      . fmap
        (\c -> if c == ',' then ' ' else c)
      <$> readFile "day6/input"
  -- %}

  -- %% -- Part 1
  print $ simulate 80 timers

  -- %% -- Part 2
  print $ simulate 256 timers
