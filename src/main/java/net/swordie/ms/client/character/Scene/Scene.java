package net.swordie.ms.client.character.Scene;

import net.swordie.ms.client.character.Char;
import net.swordie.ms.connection.packet.CField;
import net.swordie.ms.handlers.EventManager;
import net.swordie.ms.loaders.EffectData;
import net.swordie.ms.world.field.Field;
import net.swordie.ms.world.field.fieldeffect.FieldEffect;
import org.apache.log4j.LogManager;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;


/**
 * Created by Asura on 28-8-2018.
 */
public class Scene {

    private static final org.apache.log4j.Logger log = LogManager.getRootLogger();

    private Char chr;
    private String xmlPath;
    private String sceneName;
    private String sceneNumber;
    private List<EffectInfo> effectInfos;

    public Scene(Char chr, String xmlPath, String sceneName, String sceneNumber) {
        this.chr = chr;
        this.xmlPath = xmlPath;
        this.sceneName = sceneName;
        this.sceneNumber = sceneNumber;
        this.effectInfos = new ArrayList<>();
    }

    public void createScene() {
        EffectData.getEffectsFromWzPath(this);

        for (EffectInfo ei : effectInfos) {

            // Because there seem to be some type nulls that are meant to warp you.
            if(ei.getType() == null) {
                log.error(String.format("Unhandled Scene Type"));
                continue;
            }

            int delay = ei.getStart();
            String path = ei.getVisual();
            switch (ei.getType()) {
                case FieldEffect:
                    chr.write(CField.fieldEffect(FieldEffect.getFieldEffectFromWz(path+"/0", delay)));
                    break;

                case Warp:
                    Field toField = chr.getOrCreateFieldByCurrentInstanceType(ei.getField());
                    if(delay > 0) {
                        EventManager.addEvent(() -> chr.warp(toField), delay, TimeUnit.MILLISECONDS);
                    } else {
                        chr.warp(toField);
                    }
                    break;

                case playBGM:
                    // TODO
                    break;

                case unknown:
                    // TODO
                    break;
            }
        }
    }


    public String getXmlPath() {
        return xmlPath;
    }

    public void setXmlPath(String xmlPath) {
        this.xmlPath = xmlPath;
    }

    public String getSceneName() {
        return sceneName;
    }

    public void setSceneName(String sceneName) {
        this.sceneName = sceneName;
    }

    public String getSceneNumber() {
        return sceneNumber;
    }

    public void setSceneNumber(String sceneNumber) {
        this.sceneNumber = sceneNumber;
    }

    public List<EffectInfo> getEffectInfos() {
        return effectInfos;
    }

    public void setEffectInfos(List<EffectInfo> effectInfos) {
        this.effectInfos = effectInfos;
    }

    public void addEffectInfo(EffectInfo effectInfo) {
        getEffectInfos().add(effectInfo);
    }
}
