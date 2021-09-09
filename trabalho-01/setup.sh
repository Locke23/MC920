#!/bin/bash

images=()
for i in input/*.png; do
  images+=($(basename $i .png))
done

# Negative
for name in "${images[@]}"; do
  ./intensity.py 1 input/${name}.png output/${name}-negative.png
done

# Intensity reduction
for name in "${images[@]}"; do
  ./intensity.py 2 input/${name}.png output/${name}-reduced.png
done

# Brightness 1.5
for name in "${images[@]}"; do
  ./light.py 1.5 input/${name}.png output/${name}-brightness-1.5.png
done

# Brightness 2.5
for name in "${images[@]}"; do
  ./light.py 2.5 input/${name}.png output/${name}-brightness-2.5.png
done

# Brightness 3.5
for name in "${images[@]}"; do
  ./light.py 3.5 input/${name}.png output/${name}-brightness-3.5.png
done

# Quantization k in 2 4 8 16 32 64 128
for name in "${images[@]}"; do
  for k in 2 4 8 16 32 64 128; do
    ./quantization.py ${k} input/${name}.png output/${name}-quantization-${k}.png
  done
done

#Bit plane
for name in "${images[@]}"; do
  for bits in {0..7}; do
    ./bits.py ${bits} input/${name}.png output/${name}-plane-${bits}.png
  done
done

# Mosaic
for name in "${images[@]}"; do
  ./mosaic.py input/${name}.png output/${name}-mosaic.png
done

# Combine
for percentage in {0..8}; do
  ./combine.py 0.${percentage} input/${images[0]}.png input/${images[1]}.png output/${images[0]}-${images[1]}-0.${percentage}.png
done

# Filtering
for name in "${images[@]}"; do
  for filter in 1 2; do
    ./filtering.py ${filter} input/${name}.png output/${name}-filter-${filter}.png
  done
done

# Entropy calculus
for name in "${images[@]}"; do
  ./entropy_calculus.py input/"${name}".png output/"${name}"-entropy.txt
done
