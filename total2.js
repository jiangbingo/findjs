JSQEXBasicStructure.JSQEX_Room = function(a) {
    JSQEXBasicStructure.JSQEX_Loop.call(this, a);
    this.JSQEX_innerWalls = [];
    this.JSQEX_roomType = "";
    this.JSQEX_roomHeight = JSQEXBasicStructure.JSQEX_Common_Parameters.JSQEX_WallDefaultHeight;
    this.JSQEX_surf = null;
    this.JSQEX_groundPattern = null;
    this.JSQEX_groundBorder = null;
    this.JSQEX_ceilPattern = null;
    this.JSQEX_ceilBorder = null;
    this.JSQEX_areas = null;
    this.JSQEX_contents = {};
    this.JSQEX_rooms = {};
    this.JSQEX_graph = null;
    JSQEXBasicStructure.JSQEX_Room =
};