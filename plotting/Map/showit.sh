gmt begin moundMap pdf

gmt set FONT_ANNOT 15p,Helvetica,black
gmt set MAP_TICK_PEN_PRIMARY 2p


gmt grdcontour smooth.grd -R436505/436570/3671655/3671720 -JX10c/10c -C40.9,41.1,41.3,41.5,41.7,41.9,42.1,42.3,42.5,42.7,42.9,43.1,43.3,43.5,43.7,43.9,44.1,44.3,44.5,44.7,44.9,45.1,45.3,45.5,45.7,45.9 -W0.7p,150
#-C41.9,42.4,42.9,43.4,43.9,44.4,44.9,45.4,45.9 -W1p,140
#-C41.7,42.2,42.7,43.2,43.7,44.2,44.7,45.2,45.7,45.9 -W1p,140
gmt basemap -Lx8.7c/0.7c+w10+l"m" -Tdx8.7c/1.5c+w1c+l+p10 -Bnews
gmt plot SnowsMoundElecXYZ.txt -Sp0.05c -W1p

gmt plot Elec10Step.txt -S-0.3c -W2p
gmt text Elec10StepLabels.txt -D0.9/0.05

# Profile locations
# P1
gmt plot -W3 <<EOF
436534.32 3671701.07
436534.74 3671702.42
EOF
gmt text <<EOF
436537.5 3671702 P1
EOF

# P2
gmt plot -W3 <<EOF
436532.14 3671678.11
436532.44 3671679.56
EOF
gmt text <<EOF
436535 3671679 P2
EOF

# U1
gmt plot -W2 <<EOF
436545.35 3671707.12
436544.53 3671707.71
436545.66 3671709.34
436546.48 3671708.79
436545.35 3671707.12
EOF
gmt text <<EOF
436543 3671710 U1
EOF

# U2
gmt plot -W2 <<EOF
436535.43 3671686.92
436535.43 3671687.92
436536.43 3671687.92
436536.43 3671686.92
436535.43 3671686.92
EOF
gmt text <<EOF
436532.5 3671687.5 U2
EOF



gmt coast -X10.02c -Y5c -JM-70/35/5c -R-90/-75.8/25/37.2 -Dh -A1000/0/4 -W0.2p,black -N1 -N2 -S190
gmt plot -Ss0.3c -Gblack <<EOF
-87.681 33.182
EOF

#gmt grdcontour region5m.grd -R582510/584010/351710/353210 -X-0.02c -Y-5c -JX5c/5c -C33, -Bnews -Nreg.cpt
#gmt grdcontour region5m.grd -R582510/584010/351710/353210 -X-0.02c -Y-5c -JX5c/5c -C33 -W1p,140 -Bnews -Nreg.cpt

gmt grdcontour bend.grd -R-87.691/-87.668/33.168/33.1874 -JM-87.67/33.17/5c -X0c -Y-5c -C32.4 -W1p,140 -Nreg.cpt
#-R-87.691/-87.668/33.168/33.1874
gmt basemap -Lx1c/0.7c+w200e+l"m" -Bnews
gmt plot -Ss0.3c -Gblack <<EOF
-87.681 33.182
EOF
# The stupid missing line between panel a and b. Probably missing because of a bug in GMT
gmt plot -W2p,black <<EOF
-87.691 33.18735
-87.668 33.18735
EOF


gmt text -Bnews -X-10c -JX15c/10c -R0/1/0/1 --FONT_ANNOT=20,Helvetica-Bold <<EOF
0.7 0.95 a
0.7 0.45 b
0.033 0.95 c
EOF

# gmt text -Bnews -X-10c -JX15c/10c --FONT_ANNOT=20,Helvetica-Bold <<EOF
# 583550 353120 a
# 583550 352380 b
# 582550 353120 c
# EOF

# # Location markers
# gmt plot -Ss0.3c -Gblack <<EOF
# 583605 352970
# 583720 352270
# EOF

gmt end show
