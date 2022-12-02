import System.IO
import Data.List.Split
import Data.List
main = do
    lines <- readFile "1.in"
    return lines

partOne lines = maximum [sum [read z :: Integer | z <- y, length z > 0]  | y <-[splitOn "\n" x | x <- (splitOn "\n\n" lines)]] 
partTwo lines = sum $ take 3 $ reverse $ sort [sum [read z :: Integer | z <- y, length z > 0]  | y <-[splitOn "\n" x | x <- (splitOn "\n\n" lines)]]