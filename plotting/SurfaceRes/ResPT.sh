

gmt begin ResPT pdf

# create grd from the data
gmt surface ../../data/SurfaceRes/resData.txt -M1 -R436505/436571/3671646/3671720 -I0.29 -GresData.grd


gmt set FONT_ANNOT 15p,Helvetica,black
gmt set MAP_TICK_PEN_PRIMARY 2p

#gmt plot resData.txt -Sc0.08c -C -R436505/436570/3671655/3671720 -JX10c/10c
gmt grd2cpt resData.grd -Cnuuk
#gmt grdimage resData.grd -R436505/436570/3671655/3671720 -JX10c/10c
#gmt grdimage resData.grd -R436515/436555/3671662/3671712 -JX8c/10c
gmt grdimage resData.grd -R436515/436555/3671668/3671708 -JX10c/10c


gmt grdcontour smooth.grd -C41,1,41.3,41.5,41.7,41.9,42.1,42.3,42.5,42.7,42.9,43.1,43.3,43.5,43.7,43.9,44.1,44.3,44.5,44.7,44.9,45.1,45.3,45.5,45.7,45.9 -W0.7p,0
#-W0.8p,0
#-C41.7,42.7,43.7,44.7,45.7
#gmt grdcontour smooth.grd  -C41.7,42.7,43.7,44.7,45.7 -W0.8p,255
gmt basemap -Lx2.8c/0.7c+w10+l"m" -Tdx0.5c/8.6c+w1c+l+p10 -Bnews
gmt plot ../../data/SnowsMoundElecXYZ.txt -Sp0.1c -W1p
gmt plot Elec10Step.txt -S-0.4c -W2p
gmt text Elec10StepLabels.txt -D0.9/0.05
gmt colorbar -DJCR+w10c -L --FORMAT_FLOAT_MAP=%.0f
gmt text -N -F+a90 <<EOF
436564 3671688 resistance [@~W@~]
EOF
#-B+L"resistivity @~O@~"

gmt end show

