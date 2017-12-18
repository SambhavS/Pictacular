#Literal dictionary
def get_mapdict():
	dic = {(0, 0, 0): 'categories/ant/image_0023.jpg', (0, 0, 32): 'categories/electric_guitar/image_0014.jpg', (0, 0, 64): 'categories/electric_guitar/image_0014.jpg', (0, 0, 96): 'categories/headphone/image_0021.jpg', (0, 0, 128): 'categories/headphone/image_0021.jpg', (0, 0, 160): 'categories/headphone/image_0021.jpg', (0, 0, 192): 'categories/menorah/image_0075.jpg', (0, 0, 224): 'categories/menorah/image_0075.jpg', (0, 32, 0): 'categories/dragonfly/image_0031.jpg', (0, 32, 32): 'categories/electric_guitar/image_0014.jpg', (0, 32, 64): 'categories/water_lilly/image_0031.jpg', (0, 32, 96): 'categories/brain/image_0086.jpg', (0, 32, 128): 'categories/headphone/image_0021.jpg', (0, 32, 160): 'categories/hawksbill/image_0004.jpg', (0, 32, 192): 'categories/menorah/image_0075.jpg', (0, 32, 224): 'categories/menorah/image_0075.jpg', (0, 64, 0): 'categories/dragonfly/image_0031.jpg', (0, 64, 32): 'categories/bass/image_0009.jpg', (0, 64, 64): 'categories/bass/image_0018.jpg', (0, 64, 96): 'categories/brain/image_0086.jpg', (0, 64, 128): 'categories/hawksbill/image_0004.jpg', (0, 64, 160): 'categories/hawksbill/image_0004.jpg', (0, 64, 192): 'categories/hawksbill/image_0093.jpg', (0, 64, 224): 'categories/hawksbill/image_0093.jpg', (0, 96, 0): 'categories/mayfly/image_0012.jpg', (0, 96, 32): 'categories/soccer_ball/image_0021.jpg', (0, 96, 64): 'categories/brain/image_0086.jpg', (0, 96, 96): 'categories/brain/image_0086.jpg', (0, 96, 128): 'categories/metronome/image_0020.jpg', (0, 96, 160): 'categories/hawksbill/image_0048.jpg', (0, 96, 192): 'categories/hawksbill/image_0093.jpg', (0, 96, 224): 'categories/hawksbill/image_0001.jpg', (0, 128, 0): 'categories/tick/image_0028.jpg', (0, 128, 32): 'categories/dragonfly/image_0030.jpg', (0, 128, 64): 'categories/dragonfly/image_0030.jpg', (0, 128, 96): 'categories/hawksbill/image_0081.jpg', (0, 128, 128): 'categories/hawksbill/image_0081.jpg', (0, 128, 160): 'categories/anchor/image_0041.jpg', (0, 128, 192): 'categories/snoopy/image_0021.jpg', (0, 128, 224): 'categories/hawksbill/image_0001.jpg', (0, 160, 0): 'categories/tick/image_0028.jpg', (0, 160, 32): 'categories/dragonfly/image_0030.jpg', (0, 160, 64): 'categories/dragonfly/image_0030.jpg', (0, 160, 96): 'categories/hawksbill/image_0081.jpg', (0, 160, 128): 'categories/hawksbill/image_0081.jpg', (0, 160, 160): 'categories/hawksbill/image_0098.jpg', (0, 160, 192): 'categories/snoopy/image_0021.jpg', (0, 160, 224): 'categories/hawksbill/image_0001.jpg', (0, 192, 0): 'categories/mandolin/image_0014.jpg', (0, 192, 32): 'categories/gramophone/image_0038.jpg', (0, 192, 64): 'categories/gramophone/image_0038.jpg', (0, 192, 96): 'categories/hawksbill/image_0081.jpg', (0, 192, 128): 'categories/hawksbill/image_0081.jpg', (0, 192, 160): 'categories/hawksbill/image_0098.jpg', (0, 192, 192): 'categories/snoopy/image_0021.jpg', (0, 192, 224): 'categories/snoopy/image_0021.jpg', (0, 224, 0): 'categories/mandolin/image_0014.jpg', (0, 224, 32): 'categories/mandolin/image_0014.jpg', (0, 224, 64): 'categories/mandolin/image_0014.jpg', (0, 224, 96): 'categories/gramophone/image_0038.jpg', (0, 224, 128): 'categories/hawksbill/image_0081.jpg', (0, 224, 160): 'categories/umbrella/image_0072.jpg', (0, 224, 192): 'categories/umbrella/image_0072.jpg', (0, 224, 224): 'categories/umbrella/image_0072.jpg', (32, 0, 0): 'categories/lobster/image_0009.jpg', (32, 0, 32): 'categories/anchor/image_0021.jpg', (32, 0, 64): 'categories/crayfish/image_0035.jpg', (32, 0, 96): 'categories/crayfish/image_0035.jpg', (32, 0, 128): 'categories/headphone/image_0021.jpg', (32, 0, 160): 'categories/headphone/image_0021.jpg', (32, 0, 192): 'categories/menorah/image_0075.jpg', (32, 0, 224): 'categories/menorah/image_0075.jpg', (32, 32, 0): 'categories/bonsai/image_0109.jpg', (32, 32, 32): 'categories/dragonfly/image_0008.jpg', (32, 32, 64): 'categories/crayfish/image_0035.jpg', (32, 32, 96): 'categories/hawksbill/image_0039.jpg', (32, 32, 128): 'categories/headphone/image_0021.jpg', (32, 32, 160): 'categories/hawksbill/image_0004.jpg', (32, 32, 192): 'categories/menorah/image_0075.jpg', (32, 32, 224): 'categories/menorah/image_0075.jpg', (32, 64, 0): 'categories/mayfly/image_0012.jpg', (32, 64, 32): 'categories/mayfly/image_0012.jpg', (32, 64, 64): 'categories/bass/image_0018.jpg', (32, 64, 96): 'categories/sea_horse/image_0040.jpg', (32, 64, 128): 'categories/hawksbill/image_0015.jpg', (32, 64, 160): 'categories/hawksbill/image_0004.jpg', (32, 64, 192): 'categories/hawksbill/image_0093.jpg', (32, 64, 224): 'categories/hawksbill/image_0093.jpg', (32, 96, 0): 'categories/tick/image_0028.jpg', (32, 96, 32): 'categories/soccer_ball/image_0021.jpg', (32, 96, 64): 'categories/kangaroo/image_0039.jpg', (32, 96, 96): 'categories/bass/image_0038.jpg', (32, 96, 128): 'categories/revolver/image_0054.jpg', (32, 96, 160): 'categories/minaret/image_0035.jpg', (32, 96, 192): 'categories/hawksbill/image_0093.jpg', (32, 96, 224): 'categories/dolphin/image_0052.jpg', (32, 128, 0): 'categories/tick/image_0028.jpg', (32, 128, 32): 'categories/tick/image_0028.jpg', (32, 128, 64): 'categories/dragonfly/image_0030.jpg', (32, 128, 96): 'categories/pyramid/image_0014.jpg', (32, 128, 128): 'categories/ketch/image_0091.jpg', (32, 128, 160): 'categories/hawksbill/image_0098.jpg', (32, 128, 192): 'categories/snoopy/image_0021.jpg', (32, 128, 224): 'categories/crayfish/image_0031.jpg', (32, 160, 0): 'categories/tick/image_0028.jpg', (32, 160, 32): 'categories/dragonfly/image_0030.jpg', (32, 160, 64): 'categories/dragonfly/image_0030.jpg', (32, 160, 96): 'categories/hawksbill/image_0081.jpg', (32, 160, 128): 'categories/dolphin/image_0029.jpg', (32, 160, 160): 'categories/hawksbill/image_0098.jpg', (32, 160, 192): 'categories/hawksbill/image_0025.jpg', (32, 160, 224): 'categories/snoopy/image_0021.jpg', (32, 192, 0): 'categories/gramophone/image_0038.jpg', (32, 192, 32): 'categories/gramophone/image_0038.jpg', (32, 192, 64): 'categories/gramophone/image_0038.jpg', (32, 192, 96): 'categories/hawksbill/image_0081.jpg', (32, 192, 128): 'categories/ant/image_0004.jpg', (32, 192, 160): 'categories/umbrella/image_0072.jpg', (32, 192, 192): 'categories/anchor/image_0024.jpg', (32, 192, 224): 'categories/anchor/image_0024.jpg', (32, 224, 0): 'categories/mandolin/image_0014.jpg', (32, 224, 32): 'categories/mandolin/image_0014.jpg', (32, 224, 64): 'categories/gramophone/image_0038.jpg', (32, 224, 96): 'categories/gramophone/image_0038.jpg', (32, 224, 128): 'categories/ant/image_0004.jpg', (32, 224, 160): 'categories/umbrella/image_0072.jpg', (32, 224, 192): 'categories/umbrella/image_0072.jpg', (32, 224, 224): 'categories/umbrella/image_0072.jpg', (64, 0, 0): 'categories/strawberry/image_0009.jpg', (64, 0, 32): 'categories/joshua_tree/image_0011.jpg', (64, 0, 64): 'categories/joshua_tree/image_0011.jpg', (64, 0, 96): 'categories/ketch/image_0093.jpg', (64, 0, 128): 'categories/headphone/image_0021.jpg', (64, 0, 160): 'categories/headphone/image_0021.jpg', (64, 0, 192): 'categories/menorah/image_0075.jpg', (64, 0, 224): 'categories/menorah/image_0075.jpg', (64, 32, 0): 'categories/grand_piano/image_0047.jpg', (64, 32, 32): 'categories/revolver/image_0005.jpg', (64, 32, 64): 'categories/starfish/image_0035.jpg', (64, 32, 96): 'categories/ketch/image_0093.jpg', (64, 32, 128): 'categories/windsor_chair/image_0044.jpg', (64, 32, 160): 'categories/dolphin/image_0015.jpg', (64, 32, 192): 'categories/menorah/image_0075.jpg', (64, 32, 224): 'categories/menorah/image_0075.jpg', (64, 64, 0): 'categories/lotus/image_0007.jpg', (64, 64, 32): 'categories/butterfly/image_0069.jpg', (64, 64, 64): 'categories/dalmatian/image_0029.jpg', (64, 64, 96): 'categories/trilobite/image_0070.jpg', (64, 64, 128): 'categories/dolphin/image_0034.jpg', (64, 64, 160): 'categories/sea_horse/image_0001.jpg', (64, 64, 192): 'categories/wrench/image_0028.jpg', (64, 64, 224): 'categories/wrench/image_0028.jpg', (64, 96, 0): 'categories/tick/image_0028.jpg', (64, 96, 32): 'categories/mayfly/image_0014.jpg', (64, 96, 64): 'categories/cannon/image_0015.jpg', (64, 96, 96): 'categories/nautilus/image_0044.jpg', (64, 96, 128): 'categories/sea_horse/image_0011.jpg', (64, 96, 160): 'categories/dolphin/image_0008.jpg', (64, 96, 192): 'categories/wrench/image_0028.jpg', (64, 96, 224): 'categories/wrench/image_0028.jpg', (64, 128, 0): 'categories/tick/image_0028.jpg', (64, 128, 32): 'categories/garfield/image_0005.jpg', (64, 128, 64): 'categories/brain/image_0029.jpg', (64, 128, 96): 'categories/pyramid/image_0014.jpg', (64, 128, 128): 'categories/sea_horse/image_0031.jpg', (64, 128, 160): 'categories/platypus/image_0007.jpg', (64, 128, 192): 'categories/helicopter/image_0042.jpg', (64, 128, 224): 'categories/crayfish/image_0031.jpg', (64, 160, 0): 'categories/tick/image_0028.jpg', (64, 160, 32): 'categories/brain/image_0029.jpg', (64, 160, 64): 'categories/dragonfly/image_0030.jpg', (64, 160, 96): 'categories/kangaroo/image_0023.jpg', (64, 160, 128): 'categories/lobster/image_0040.jpg', (64, 160, 160): 'categories/lobster/image_0040.jpg', (64, 160, 192): 'categories/anchor/image_0024.jpg', (64, 160, 224): 'categories/anchor/image_0024.jpg', (64, 192, 0): 'categories/gramophone/image_0038.jpg', (64, 192, 32): 'categories/gramophone/image_0038.jpg', (64, 192, 64): 'categories/gramophone/image_0038.jpg', (64, 192, 96): 'categories/yin_yang/image_0056.jpg', (64, 192, 128): 'categories/ant/image_0004.jpg', (64, 192, 160): 'categories/umbrella/image_0072.jpg', (64, 192, 192): 'categories/anchor/image_0024.jpg', (64, 192, 224): 'categories/anchor/image_0024.jpg', (64, 224, 0): 'categories/mandolin/image_0014.jpg', (64, 224, 32): 'categories/gramophone/image_0038.jpg', (64, 224, 64): 'categories/gramophone/image_0038.jpg', (64, 224, 96): 'categories/yin_yang/image_0056.jpg', (64, 224, 128): 'categories/ant/image_0004.jpg', (64, 224, 160): 'categories/umbrella/image_0072.jpg', (64, 224, 192): 'categories/umbrella/image_0072.jpg', (64, 224, 224): 'categories/umbrella/image_0072.jpg', (96, 0, 0): 'categories/stop_sign/image_0027.jpg', (96, 0, 32): 'categories/stop_sign/image_0027.jpg', (96, 0, 64): 'categories/stop_sign/image_0032.jpg', (96, 0, 96): 'categories/snoopy/image_0003.jpg', (96, 0, 128): 'categories/dolphin/image_0015.jpg', (96, 0, 160): 'categories/dolphin/image_0015.jpg', (96, 0, 192): 'categories/menorah/image_0075.jpg', (96, 0, 224): 'categories/menorah/image_0075.jpg', (96, 32, 0): 'categories/stop_sign/image_0027.jpg', (96, 32, 32): 'categories/strawberry/image_0007.jpg', (96, 32, 64): 'categories/snoopy/image_0003.jpg', (96, 32, 96): 'categories/snoopy/image_0003.jpg', (96, 32, 128): 'categories/dolphin/image_0015.jpg', (96, 32, 160): 'categories/dolphin/image_0015.jpg', (96, 32, 192): 'categories/wrench/image_0028.jpg', (96, 32, 224): 'categories/wrench/image_0028.jpg', (96, 64, 0): 'categories/sunflower/image_0076.jpg', (96, 64, 32): 'categories/sunflower/image_0006.jpg', (96, 64, 64): 'categories/lotus/image_0033.jpg', (96, 64, 96): 'categories/crab/image_0069.jpg', (96, 64, 128): 'categories/dolphin/image_0015.jpg', (96, 64, 160): 'categories/dolphin/image_0014.jpg', (96, 64, 192): 'categories/wrench/image_0028.jpg', (96, 64, 224): 'categories/wrench/image_0028.jpg', (96, 96, 0): 'categories/sunflower/image_0076.jpg', (96, 96, 32): 'categories/sunflower/image_0041.jpg', (96, 96, 64): 'categories/wild_cat/image_0032.jpg', (96, 96, 96): 'categories/binocular/image_0030.jpg', (96, 96, 128): 'categories/ferry/image_0031.jpg', (96, 96, 160): 'categories/hawksbill/image_0044.jpg', (96, 96, 192): 'categories/ketch/image_0072.jpg', (96, 96, 224): 'categories/camera/image_0036.jpg', (96, 128, 0): 'categories/garfield/image_0005.jpg', (96, 128, 32): 'categories/butterfly/image_0038.jpg', (96, 128, 64): 'categories/kangaroo/image_0072.jpg', (96, 128, 96): 'categories/chandelier/image_0101.jpg', (96, 128, 128): 'categories/soccer_ball/image_0001.jpg', (96, 128, 160): 'categories/watch/image_0158.jpg', (96, 128, 192): 'categories/ketch/image_0054.jpg', (96, 128, 224): 'categories/ketch/image_0050.jpg', (96, 160, 0): 'categories/garfield/image_0005.jpg', (96, 160, 32): 'categories/garfield/image_0005.jpg', (96, 160, 64): 'categories/lotus/image_0063.jpg', (96, 160, 96): 'categories/flamingo_head/image_0005.jpg', (96, 160, 128): 'categories/crayfish/image_0048.jpg', (96, 160, 160): 'categories/crayfish/image_0046.jpg', (96, 160, 192): 'categories/helicopter/image_0029.jpg', (96, 160, 224): 'categories/anchor/image_0017.jpg', (96, 192, 0): 'categories/gramophone/image_0038.jpg', (96, 192, 32): 'categories/gramophone/image_0038.jpg', (96, 192, 64): 'categories/yin_yang/image_0056.jpg', (96, 192, 96): 'categories/yin_yang/image_0056.jpg', (96, 192, 128): 'categories/ant/image_0004.jpg', (96, 192, 160): 'categories/ketch/image_0062.jpg', (96, 192, 192): 'categories/helicopter/image_0081.jpg', (96, 192, 224): 'categories/tick/image_0038.jpg', (96, 224, 0): 'categories/gramophone/image_0038.jpg', (96, 224, 32): 'categories/gramophone/image_0038.jpg', (96, 224, 64): 'categories/yin_yang/image_0056.jpg', (96, 224, 96): 'categories/yin_yang/image_0056.jpg', (96, 224, 128): 'categories/ant/image_0004.jpg', (96, 224, 160): 'categories/umbrella/image_0072.jpg', (96, 224, 192): 'categories/umbrella/image_0072.jpg', (96, 224, 224): 'categories/tick/image_0038.jpg', (128, 0, 0): 'categories/stop_sign/image_0027.jpg', (128, 0, 32): 'categories/strawberry/image_0007.jpg', (128, 0, 64): 'categories/cellphone/image_0006.jpg', (128, 0, 96): 'categories/metronome/image_0009.jpg', (128, 0, 128): 'categories/snoopy/image_0003.jpg', (128, 0, 160): 'categories/dolphin/image_0015.jpg', (128, 0, 192): 'categories/dolphin/image_0014.jpg', (128, 0, 224): 'categories/camera/image_0036.jpg', (128, 32, 0): 'categories/strawberry/image_0010.jpg', (128, 32, 32): 'categories/cannon/image_0022.jpg', (128, 32, 64): 'categories/metronome/image_0009.jpg', (128, 32, 96): 'categories/metronome/image_0009.jpg', (128, 32, 128): 'categories/brain/image_0042.jpg', (128, 32, 160): 'categories/dolphin/image_0014.jpg', (128, 32, 192): 'categories/dolphin/image_0014.jpg', (128, 32, 224): 'categories/camera/image_0036.jpg', (128, 64, 0): 'categories/trilobite/image_0024.jpg', (128, 64, 32): 'categories/pizza/image_0005.jpg', (128, 64, 64): 'categories/stop_sign/image_0045.jpg', (128, 64, 96): 'categories/strawberry/image_0011.jpg', (128, 64, 128): 'categories/pyramid/image_0002.jpg', (128, 64, 160): 'categories/dolphin/image_0014.jpg', (128, 64, 192): 'categories/camera/image_0036.jpg', (128, 64, 224): 'categories/camera/image_0036.jpg', (128, 96, 0): 'categories/sunflower/image_0008.jpg', (128, 96, 32): 'categories/sunflower/image_0027.jpg', (128, 96, 64): 'categories/chandelier/image_0089.jpg', (128, 96, 96): 'categories/panda/image_0026.jpg', (128, 96, 128): 'categories/stop_sign/image_0014.jpg', (128, 96, 160): 'categories/joshua_tree/image_0007.jpg', (128, 96, 192): 'categories/camera/image_0036.jpg', (128, 96, 224): 'categories/camera/image_0036.jpg', (128, 128, 0): 'categories/sunflower/image_0024.jpg', (128, 128, 32): 'categories/kangaroo/image_0048.jpg', (128, 128, 64): 'categories/dragonfly/image_0068.jpg', (128, 128, 96): 'categories/hawksbill/image_0045.jpg', (128, 128, 128): 'categories/brain/image_0097.jpg', (128, 128, 160): 'categories/ketch/image_0088.jpg', (128, 128, 192): 'categories/schooner/image_0053.jpg', (128, 128, 224): 'categories/camera/image_0036.jpg', (128, 160, 0): 'categories/sunflower/image_0024.jpg', (128, 160, 32): 'categories/sunflower/image_0030.jpg', (128, 160, 64): 'categories/platypus/image_0027.jpg', (128, 160, 96): 'categories/ibis/image_0068.jpg', (128, 160, 128): 'categories/bonsai/image_0086.jpg', (128, 160, 160): 'categories/headphone/image_0040.jpg', (128, 160, 192): 'categories/dolphin/image_0065.jpg', (128, 160, 224): 'categories/ketch/image_0040.jpg', (128, 192, 0): 'categories/butterfly/image_0041.jpg', (128, 192, 32): 'categories/sunflower/image_0030.jpg', (128, 192, 64): 'categories/sunflower/image_0030.jpg', (128, 192, 96): 'categories/crab/image_0003.jpg', (128, 192, 128): 'categories/pigeon/image_0032.jpg', (128, 192, 160): 'categories/dragonfly/image_0043.jpg', (128, 192, 192): 'categories/helicopter/image_0081.jpg', (128, 192, 224): 'categories/okapi/image_0038.jpg', (128, 224, 0): 'categories/butterfly/image_0041.jpg', (128, 224, 32): 'categories/cellphone/image_0035.jpg', (128, 224, 64): 'categories/yin_yang/image_0056.jpg', (128, 224, 96): 'categories/crab/image_0003.jpg', (128, 224, 128): 'categories/nautilus/image_0016.jpg', (128, 224, 160): 'categories/dragonfly/image_0043.jpg', (128, 224, 192): 'categories/tick/image_0037.jpg', (128, 224, 224): 'categories/tick/image_0037.jpg', (160, 0, 0): 'categories/strawberry/image_0010.jpg', (160, 0, 32): 'categories/cellphone/image_0006.jpg', (160, 0, 64): 'categories/cellphone/image_0006.jpg', (160, 0, 96): 'categories/metronome/image_0009.jpg', (160, 0, 128): 'categories/panda/image_0010.jpg', (160, 0, 160): 'categories/panda/image_0010.jpg', (160, 0, 192): 'categories/starfish/image_0041.jpg', (160, 0, 224): 'categories/starfish/image_0041.jpg', (160, 32, 0): 'categories/strawberry/image_0010.jpg', (160, 32, 32): 'categories/cellphone/image_0006.jpg', (160, 32, 64): 'categories/metronome/image_0009.jpg', (160, 32, 96): 'categories/panda/image_0010.jpg', (160, 32, 128): 'categories/panda/image_0010.jpg', (160, 32, 160): 'categories/gramophone/image_0050.jpg', (160, 32, 192): 'categories/starfish/image_0041.jpg', (160, 32, 224): 'categories/starfish/image_0041.jpg', (160, 64, 0): 'categories/stop_sign/image_0041.jpg', (160, 64, 32): 'categories/kangaroo/image_0044.jpg', (160, 64, 64): 'categories/pizza/image_0014.jpg', (160, 64, 96): 'categories/panda/image_0010.jpg', (160, 64, 128): 'categories/buddha/image_0024.jpg', (160, 64, 160): 'categories/gramophone/image_0050.jpg', (160, 64, 192): 'categories/joshua_tree/image_0007.jpg', (160, 64, 224): 'categories/camera/image_0036.jpg', (160, 96, 0): 'categories/sunflower/image_0051.jpg', (160, 96, 32): 'categories/strawberry/image_0001.jpg', (160, 96, 64): 'categories/sea_horse/image_0043.jpg', (160, 96, 96): 'categories/dalmatian/image_0003.jpg', (160, 96, 128): 'categories/water_lilly/image_0005.jpg', (160, 96, 160): 'categories/pyramid/image_0031.jpg', (160, 96, 192): 'categories/dolphin/image_0047.jpg', (160, 96, 224): 'categories/camera/image_0036.jpg', (160, 128, 0): 'categories/sunflower/image_0051.jpg', (160, 128, 32): 'categories/sunflower/image_0031.jpg', (160, 128, 64): 'categories/cougar_body/image_0028.jpg', (160, 128, 96): 'categories/pizza/image_0020.jpg', (160, 128, 128): 'categories/trilobite/image_0052.jpg', (160, 128, 160): 'categories/umbrella/image_0034.jpg', (160, 128, 192): 'categories/dolphin/image_0047.jpg', (160, 128, 224): 'categories/lotus/image_0034.jpg', (160, 160, 0): 'categories/butterfly/image_0041.jpg', (160, 160, 32): 'categories/sunflower/image_0079.jpg', (160, 160, 64): 'categories/sunflower/image_0085.jpg', (160, 160, 96): 'categories/kangaroo/image_0046.jpg', (160, 160, 128): 'categories/wild_cat/image_0020.jpg', (160, 160, 160): 'categories/umbrella/image_0045.jpg', (160, 160, 192): 'categories/crocodile_head/image_0028.jpg', (160, 160, 224): 'categories/lotus/image_0034.jpg', (160, 192, 0): 'categories/butterfly/image_0041.jpg', (160, 192, 32): 'categories/cellphone/image_0035.jpg', (160, 192, 64): 'categories/cellphone/image_0035.jpg', (160, 192, 96): 'categories/kangaroo/image_0077.jpg', (160, 192, 128): 'categories/nautilus/image_0016.jpg', (160, 192, 160): 'categories/butterfly/image_0018.jpg', (160, 192, 192): 'categories/buddha/image_0040.jpg', (160, 192, 224): 'categories/ketch/image_0070.jpg', (160, 224, 0): 'categories/butterfly/image_0041.jpg', (160, 224, 32): 'categories/cellphone/image_0035.jpg', (160, 224, 64): 'categories/cellphone/image_0035.jpg', (160, 224, 96): 'categories/kangaroo/image_0077.jpg', (160, 224, 128): 'categories/nautilus/image_0016.jpg', (160, 224, 160): 'categories/yin_yang/image_0003.jpg', (160, 224, 192): 'categories/snoopy/image_0008.jpg', (160, 224, 224): 'categories/snoopy/image_0008.jpg', (192, 0, 0): 'categories/windsor_chair/image_0048.jpg', (192, 0, 32): 'categories/windsor_chair/image_0048.jpg', (192, 0, 64): 'categories/windsor_chair/image_0048.jpg', (192, 0, 96): 'categories/panda/image_0010.jpg', (192, 0, 128): 'categories/panda/image_0010.jpg', (192, 0, 160): 'categories/starfish/image_0041.jpg', (192, 0, 192): 'categories/starfish/image_0041.jpg', (192, 0, 224): 'categories/starfish/image_0041.jpg', (192, 32, 0): 'categories/windsor_chair/image_0048.jpg', (192, 32, 32): 'categories/garfield/image_0007.jpg', (192, 32, 64): 'categories/stop_sign/image_0063.jpg', (192, 32, 96): 'categories/panda/image_0010.jpg', (192, 32, 128): 'categories/panda/image_0010.jpg', (192, 32, 160): 'categories/gramophone/image_0050.jpg', (192, 32, 192): 'categories/starfish/image_0041.jpg', (192, 32, 224): 'categories/starfish/image_0041.jpg', (192, 64, 0): 'categories/garfield/image_0007.jpg', (192, 64, 32): 'categories/garfield/image_0007.jpg', (192, 64, 64): 'categories/panda/image_0031.jpg', (192, 64, 96): 'categories/panda/image_0010.jpg', (192, 64, 128): 'categories/gramophone/image_0050.jpg', (192, 64, 160): 'categories/gramophone/image_0050.jpg', (192, 64, 192): 'categories/starfish/image_0041.jpg', (192, 64, 224): 'categories/starfish/image_0041.jpg', (192, 96, 0): 'categories/pyramid/image_0017.jpg', (192, 96, 32): 'categories/stop_sign/image_0026.jpg', (192, 96, 64): 'categories/bonsai/image_0036.jpg', (192, 96, 96): 'categories/stop_sign/image_0006.jpg', (192, 96, 128): 'categories/gramophone/image_0050.jpg', (192, 96, 160): 'categories/gramophone/image_0050.jpg', (192, 96, 192): 'categories/pigeon/image_0023.jpg', (192, 96, 224): 'categories/pigeon/image_0023.jpg', (192, 128, 0): 'categories/pyramid/image_0017.jpg', (192, 128, 32): 'categories/buddha/image_0041.jpg', (192, 128, 64): 'categories/scissors/image_0019.jpg', (192, 128, 96): 'categories/pizza/image_0012.jpg', (192, 128, 128): 'categories/stop_sign/image_0012.jpg', (192, 128, 160): 'categories/snoopy/image_0032.jpg', (192, 128, 192): 'categories/pigeon/image_0023.jpg', (192, 128, 224): 'categories/lotus/image_0034.jpg', (192, 160, 0): 'categories/butterfly/image_0041.jpg', (192, 160, 32): 'categories/garfield/image_0024.jpg', (192, 160, 64): 'categories/sunflower/image_0054.jpg', (192, 160, 96): 'categories/sunflower/image_0052.jpg', (192, 160, 128): 'categories/crab/image_0055.jpg', (192, 160, 160): 'categories/tick/image_0041.jpg', (192, 160, 192): 'categories/crocodile_head/image_0032.jpg', (192, 160, 224): 'categories/pyramid/image_0008.jpg', (192, 192, 0): 'categories/butterfly/image_0041.jpg', (192, 192, 32): 'categories/butterfly/image_0041.jpg', (192, 192, 64): 'categories/ibis/image_0071.jpg', (192, 192, 96): 'categories/pyramid/image_0006.jpg', (192, 192, 128): 'categories/umbrella/image_0051.jpg', (192, 192, 160): 'categories/gramophone/image_0051.jpg', (192, 192, 192): 'categories/euphonium/image_0014.jpg', (192, 192, 224): 'categories/lamp/image_0048.jpg', (192, 224, 0): 'categories/butterfly/image_0041.jpg', (192, 224, 32): 'categories/butterfly/image_0041.jpg', (192, 224, 64): 'categories/sunflower/image_0049.jpg', (192, 224, 96): 'categories/pyramid/image_0006.jpg', (192, 224, 128): 'categories/dragonfly/image_0016.jpg', (192, 224, 160): 'categories/snoopy/image_0004.jpg', (192, 224, 192): 'categories/buddha/image_0011.jpg', (192, 224, 224): 'categories/ketch/image_0112.jpg', (224, 0, 0): 'categories/windsor_chair/image_0049.jpg', (224, 0, 32): 'categories/windsor_chair/image_0049.jpg', (224, 0, 64): 'categories/crayfish/image_0041.jpg', (224, 0, 96): 'categories/revolver/image_0013.jpg', (224, 0, 128): 'categories/panda/image_0010.jpg', (224, 0, 160): 'categories/starfish/image_0041.jpg', (224, 0, 192): 'categories/starfish/image_0041.jpg', (224, 0, 224): 'categories/starfish/image_0041.jpg', (224, 32, 0): 'categories/windsor_chair/image_0049.jpg', (224, 32, 32): 'categories/crayfish/image_0041.jpg', (224, 32, 64): 'categories/revolver/image_0013.jpg', (224, 32, 96): 'categories/stop_sign/image_0016.jpg', (224, 32, 128): 'categories/snoopy/image_0027.jpg', (224, 32, 160): 'categories/starfish/image_0041.jpg', (224, 32, 192): 'categories/starfish/image_0041.jpg', (224, 32, 224): 'categories/starfish/image_0041.jpg', (224, 64, 0): 'categories/garfield/image_0007.jpg', (224, 64, 32): 'categories/brain/image_0073.jpg', (224, 64, 64): 'categories/stop_sign/image_0016.jpg', (224, 64, 96): 'categories/stop_sign/image_0057.jpg', (224, 64, 128): 'categories/snoopy/image_0027.jpg', (224, 64, 160): 'categories/snoopy/image_0027.jpg', (224, 64, 192): 'categories/starfish/image_0041.jpg', (224, 64, 224): 'categories/starfish/image_0041.jpg', (224, 96, 0): 'categories/pyramid/image_0017.jpg', (224, 96, 32): 'categories/stop_sign/image_0010.jpg', (224, 96, 64): 'categories/strawberry/image_0012.jpg', (224, 96, 96): 'categories/stop_sign/image_0057.jpg', (224, 96, 128): 'categories/strawberry/image_0018.jpg', (224, 96, 160): 'categories/stop_sign/image_0015.jpg', (224, 96, 192): 'categories/pigeon/image_0023.jpg', (224, 96, 224): 'categories/starfish/image_0041.jpg', (224, 128, 0): 'categories/ant/image_0040.jpg', (224, 128, 32): 'categories/buddha/image_0041.jpg', (224, 128, 64): 'categories/snoopy/image_0034.jpg', (224, 128, 96): 'categories/snoopy/image_0031.jpg', (224, 128, 128): 'categories/yin_yang/image_0045.jpg', (224, 128, 160): 'categories/stop_sign/image_0053.jpg', (224, 128, 192): 'categories/pigeon/image_0023.jpg', (224, 128, 224): 'categories/starfish/image_0071.jpg', (224, 160, 0): 'categories/ant/image_0040.jpg', (224, 160, 32): 'categories/garfield/image_0023.jpg', (224, 160, 64): 'categories/emu/image_0043.jpg', (224, 160, 96): 'categories/emu/image_0043.jpg', (224, 160, 128): 'categories/strawberry/image_0031.jpg', (224, 160, 160): 'categories/butterfly/image_0053.jpg', (224, 160, 192): 'categories/stop_sign/image_0003.jpg', (224, 160, 224): 'categories/starfish/image_0071.jpg', (224, 192, 0): 'categories/ant/image_0040.jpg', (224, 192, 32): 'categories/garfield/image_0023.jpg', (224, 192, 64): 'categories/lotus/image_0035.jpg', (224, 192, 96): 'categories/tick/image_0027.jpg', (224, 192, 128): 'categories/sunflower/image_0070.jpg', (224, 192, 160): 'categories/pizza/image_0031.jpg', (224, 192, 192): 'categories/stop_sign/image_0019.jpg', (224, 192, 224): 'categories/starfish/image_0071.jpg', (224, 224, 0): 'categories/ant/image_0040.jpg', (224, 224, 32): 'categories/lotus/image_0035.jpg', (224, 224, 64): 'categories/sunflower/image_0071.jpg', (224, 224, 96): 'categories/tick/image_0027.jpg', (224, 224, 128): 'categories/pyramid/image_0004.jpg', (224, 224, 160): 'categories/snoopy/image_0018.jpg', (224, 224, 192): 'categories/strawberry/image_0034.jpg', (224, 224, 224): 'categories/dalmatian/image_0004.jpg'}
	return dic

"""
#Code to get the above dictionary
def setup(self):
		def dist(tup1,tup2):
			return sqrt((tup1[0]-tup2[0])**2 + (tup1[1]-tup2[1])**2 + (tup1[2]-tup2[2])**2)
		#get color averages & files
		base =categories"  #input("Please enter path to image libary: ")
		#Code should be modified if user has different file structure.
		folder_names = os.listdir(base)
		pics_and_cols = []
		lower="qwertyuiopasdfghjklzxcvbnm"
		for f_name in folder_names:
			if f_name[0] in lower:
				pic_names = os.listdir(base+"/"+f_name)
				for p_name in pic_names:
					if p_name[0] in lower:
						path = base+"/"+f_name+"/"+p_name
						pic = Image.open(path)
						pair = self.get_pair(pic)
						#pair will be None, if image is not square enough
						if pair:
							pics_and_cols.append((path,pair[0],pair[1]))
		#populate zone/image dictionary
		for r in range(0,256,32):
			for g in range(0,256,32):
				for b in range(0,256,32):
					zone = (r,g,b)
					self.zones_and_images[zone] = min(pics_and_cols, key = lambda entry: dist(entry[2],zone))[:2]
""" 