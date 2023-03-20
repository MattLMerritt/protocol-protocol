#ifndef __SCENE_H__
#define __SCENE_H__

#include <list>

#include <frame.h>
#include <timer.h>

/* Scene

*/

class Scene {
    public:
        Scene();

        // initialize the scene
        void initScene();

    private:
        Timer timer;
        std::list<Frame> frames; // replace this later with a more efficient option

};

#endif