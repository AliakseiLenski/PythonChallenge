import viz
import vizact

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#Add the environment
dojo = viz.addChild('dojo.osgb')
#lobby = vizfx.addChild('lobby.osgb')

#Add an avatar
male = viz.addAvatar('vcc_male.cfg', pos=(-2,0,0), euler=(90,0,0) )
female = viz.addAvatar('vcc_female.cfg')
crate = viz.addChild('crate.osgb',pos=[-1,0.25,2], scale=[0.5,0.5,0.5])
childPigeon = viz.addAvatar('pigeon.cfg', scale=[0.8,0.8,0.8])
worldPigeon = viz.addAvatar('pigeon.cfg', scale=[0.8,0.8,0.8])

childPigeon.setPosition([-1,0.5,2.15], viz.ABS_GLOBAL)
worldPigeon.setPosition([-1,0.5,1.85])
childPigeon.setEuler([150,0,0])



female.setPosition([4,0,-2])
female.setEuler([-90,0,0])

#Move the viewpoint
viz.MainView.setPosition([2,1.8,0])
viz.MainView.setEuler([-140,0,0])
viz.MainView.setPosition([5,1.8,3.5])

vizact.onkeydown('1', male.state, 5)
vizact.onkeydown('2', female.state, 6)
vizact.onkeydown('3', male.speed, .5)
vizact.onkeydown('4', female.speed, .5)

def heDances():
    male.addAction( vizact.animation(5) )

def sheShouts():
    female.addAction( vizact.animation(3) )
def theyDance():
	male.addAction( vizact.animation(14) )
	female.addAction( vizact.animation(14) )


walk_over = vizact.walkTo([1.9,0,-1.86])
male.addAction(walk_over)
heDances()
sheShouts()
theyDance()